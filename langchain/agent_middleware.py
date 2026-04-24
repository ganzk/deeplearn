# 中间件
from langchain.agents.middleware import SummarizationMiddleware, HumanInTheLoopMiddleware, ModelCallLimitMiddleware, \
    ToolCallLimitMiddleware, ModelFallbackMiddleware, PIIMiddleware, TodoListMiddleware, LLMToolSelectorMiddleware, \
    ToolRetryMiddleware, LLMToolEmulator, ContextEditingMiddleware, ClearToolUsesEdit
from langchain_openai import ChatOpenAI

# 配置 DeepSeek 的 API 信息
basic_model = ChatOpenAI(
    model="deepseek-chat",  # 或使用 "deepseek-reasoner"（推理模型）
    openai_api_key="sk-9057255f494b4076b774b1a617491e55",  # 你的 DeepSeek API Key
    openai_api_base="https://api.deepseek.com/v1",  # DeepSeek 的 API 地址
    temperature=0.7,
    max_tokens=1024
)

# 记忆  总结消息
# 除了下面的参数，还有其他值
# token_counter: 函数，自定义 token 计数函数。默认为基于字符的计数。
# summary_prompt: 字符串，自定义提示词模板。如果未指定，则使用内置模板。
# summary_prefix: 字符串 (默认值: "## Previous conversation summary:")，摘要消息的前缀。
summarization = SummarizationMiddleware(
            model=basic_model,  # 用于生成摘要的模型
            max_tokens_before_summary=4000,  # 数字，触发摘要的 token 阈值。
            messages_to_keep=20,  # 要保留的最新消息数量，默认20
        )


# 在工具执行之前，暂停代理执行以供人工批准、编辑或拒绝工具调用。
# interrupt_on: 字典 (必需)，工具名称到批准配置的映射。值可以是 True（使用默认配置中断）、False（自动批准）或一个 InterruptOnConfig 对象。
# description_prefix: 字符串 (默认值: "Tool execution requires approval")，操作请求描述的前缀。

# InterruptOnConfig 选项：
# allowed_decisions: 字符串列表，允许的决定列表："approve"、"edit" 或 "reject"。
# description: 字符串 | 可调用对象，用于自定义描述的静态字符串或可调用函数。
humInTheLoop = HumanInTheLoopMiddleware(
            interrupt_on={
                # 要求对发送邮件进行批准、编辑或拒绝
                "calculator": {
                    "allowed_decisions": ["approve", "edit", "reject"],
                },
                # 自动批准读取邮件
                "read_email_tool": False,
            }
        )




# 限制模型调用
modelCallLimit = ModelCallLimitMiddleware(
            thread_limit=10,  # 每个线程（跨多次运行）最多 10 次调用
            run_limit=5,  # 每次运行（单次调用）最多 5 次调用
            exit_behavior="end",  # 或者 "error" 以引发异常
        )




# 限制工具调用
# tool_name: 字符串，要限制的特定工具。如果未提供，则限制适用于所有工具。
# thread_limit: 数字，线程中所有运行的最大工具调用次数。默认为无限制。
# run_limit: 数字，单次调用中最大工具调用次数。默认为无限制。
# exit_behavior: 字符串 (默认值: "end")，达到限制时的行为。选项："end"（优雅终止）或 "error"（引发异常）。
# 限制所有工具调用
global_limiter = ToolCallLimitMiddleware(thread_limit=20, run_limit=10)

# 限制特定工具
search_limiter = ToolCallLimitMiddleware(
    tool_name="search",
    thread_limit=5,
    run_limit=3,
)


# 模型回退，当主要模型失败时，自动回退到替代模型。
modelFallback = ModelFallbackMiddleware(
            basic_model,  # 错误时首先尝试
            "anthropic:claude-3-5-sonnet-20241022",  # 然后尝试这个
        )

# 检测和处理对话中的个人身份信息

# 涂改用户输入中的电子邮件
PIIMiddleware("email", strategy="redact", apply_to_input=True)
# 掩盖信用卡（显示后 4 位）
PIIMiddleware("credit_card", strategy="mask", apply_to_input=True)
# 带有正则表达式的自定义 PII 类型
PIIMiddleware(
    "api_key",
    detector=r"sk-[a-zA-Z0-9]{32}",
    strategy="block",  # 如果检测到，则引发错误
)

# 为复杂的多步骤任务添加待办事项列表管理功能。
todoLis = TodoListMiddleware()


# 在调用主模型之前，使用 LLM 智能地选择相关工具。
llmToolSelector = LLMToolSelectorMiddleware(
            model="openai:gpt-4o-mini",  # 使用更便宜的模型进行选择
            max_tools=3,  # 限制为 3 个最相关的工具
            always_include=["search"],  # 始终包含某些工具
        )



# 工具重试 使用可配置的指数回退自动重试失败的工具调用。
toolRetry = ToolRetryMiddleware(
            max_retries=3,  # 最多重试 3 次
            backoff_factor=2.0,  # 指数回退乘数
            initial_delay=1.0,  # 从 1 秒延迟开始
            max_delay=60.0,  # 将延迟上限设置为 60 秒
            jitter=True,  # 添加随机抖动以避免“惊群”问题
        )


# LLM 工具模拟器 (LLM tool emulator)
# 使用 LLM 模拟工具执行，用于测试目的，用 AI 生成的响应替换实际工具调用。
llmToolEmulator = LLMToolEmulator(),

# 或模拟特定工具
# LLMToolEmulator(tools=["get_weather", "search_database"]),

# 或使用自定义模型进行模拟
# LLMToolEmulator(model="anthropic:claude-3-5-sonnet-latest"),


# 上下文编辑
# 通过修剪、摘要或清除工具使用来管理对话上下文。
contextEditing = ContextEditingMiddleware(
            edits=[
                ClearToolUsesEdit(max_tokens=1000),  # 清除旧的工具使用
            ],
        )



## 自定义中间件
# 基于装饰器的中间件
# @before_model  节点式 (Node-style)：模型调用前的日志记录
# @after_model(can_jump_to=["end"])  节点式 (Node-style)：模型调用后的验证
# @wrap_model_call  包装式 (Wrap-style)：重试逻辑
# @dynamic_prompt  包装式 (Wrap-style)：动态提示词
# @before_agent 代理启动前（每次调用一次）
# @after_agent 代理完成时（每次调用最多一次）
# @wrap_tool_call 每次工具调用周围
# 执行流程： before_agent -》 before_model -》 after_model -》 after_agent























