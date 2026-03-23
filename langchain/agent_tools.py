from typing import Any

from langchain.agents import create_agent, AgentState
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse, dynamic_prompt, \
    SummarizationMiddleware, before_model
from langchain.agents.structured_output import ToolStrategy, ProviderStrategy

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage, RemoveMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.tools import tool
from langgraph.graph.message import REMOVE_ALL_MESSAGES
from langgraph.runtime import Runtime

from toolsBase import MyAgentTool, ContactInfo


@tool
def multiply(a: int, b: int) -> int:
    """将两个整数相乘。"""
    return a * b


# 配置 DeepSeek 的 API 信息
basic_model = ChatOpenAI(
    model="deepseek-chat",  # 或使用 "deepseek-reasoner"（推理模型）
    openai_api_key="sk-9057255f494b4076b774b1a617491e55",  # 你的 DeepSeek API Key
    openai_api_base="https://api.deepseek.com/v1",  # DeepSeek 的 API 地址
    temperature=0.7,
    max_tokens=1024
)

advanced_model = ChatOpenAI(
    model="deepseek-reasoner",  # 或使用 "deepseek-reasoner"（推理模型）
    openai_api_key="sk-9057255f494b4076b774b1a617491e55",  # 你的 DeepSeek API Key
    openai_api_base="https://api.deepseek.com/v1",  # DeepSeek 的 API 地址
    temperature=0.7,
    max_tokens=1024
)

# 动态模型(中间件，在调用模型的时候，可以处理调用细节)
@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """根据对话复杂性选择模型。"""
    message_count = len(request.state["messages"])

    if message_count > 10:
        # 对较长的对话使用高级模型
        print("使用advanced_model")
        model = advanced_model
    else:
        model = basic_model
        print("使用basic_model")

    request.model = model
    return handler(request)


# 工具-注解调用
@tool
def search(query: str) -> str:
    """搜索信息。"""
    return f"结果：{query}"

@tool
def get_weather(location: str) -> str:
    """获取位置的天气信息。"""
    return f"{location} 的天气：晴朗，72°F"

# 工具-继承BaseTool方式创建
calculator = MyAgentTool()


# 系统提示词
system_prompt = '''你现在是一名专业的A股投资内容解读专家，
    **核心任务**
    是把股票大V发布的晦涩文章、行业黑话、拐弯抹角的暗示，翻译成散户能看懂的大白话，精准拆解出作者的真实意图.

    **严格遵守以下要求：**
    1. 先给出核心结论：作者这篇文章整体是利多还是利空？明确指出作者暗戳戳推荐买入的标的/板块，以及作者明确提示风险、让大家别碰的标的/板块，不能有任何模棱两可的表述；
    2. 再做逐段大白话翻译：把原文每一段的真实意思，用最直白的话讲清楚，去掉所有弯弯绕绕、专业黑话，只保留最核心的信息；
    3. 拆解作者的底层逻辑：讲清楚作者看好/看空这个标的/板块的核心理由是什么，他的逻辑链条是什么，不能只结论不说原因；
    4. 补充风险提示：把原文里作者没明说、但隐藏的投资风险，明确标注出来，提醒散户注意避坑；
    5. 全程只用大白话，不用任何专业术语，不搞弯弯绕绕，精准、直白、不模棱两可。
    6. 如果有不清楚的地方，可以通过联网检索

    现在请你按照以上要求，解读下面的文章内容：'''

# 动态提示词
@dynamic_prompt
def user_role_prompt(request: ModelRequest) -> str:
    """根据用户角色生成系统提示。"""
    ## 还可以将传递的入参，拼接到提示词中去
    print("request.runtime.context:", request.runtime.context)
    user_role = request.runtime.context.get("user_role", "user")
    base_prompt = "你是一个有帮助的助手。当用户存在多个意图时，请分别为每个独立意图调用工具，而不是试图在一个工具调用中完成所有任务。"

    if user_role == "expert":
        return f"{base_prompt} 提供详细的技术响应。"
    elif user_role == "beginner":
        return f"{base_prompt} 简单解释概念，避免使用行话。"

    return base_prompt


# 格式化输出
toolStrategy = ProviderStrategy (ContactInfo)

# 记忆  总结消息
summarization = SummarizationMiddleware(
            model=basic_model,  # 用于生成摘要的模型
            max_tokens_before_summary=4000,  # 任一条件触发
            messages_to_keep=20,  # 触发后保留最近20条原始消息
        )

# 使用自定义AgentState扩展额外字段，默认情况下代理使用 AgentState 来管理短期记忆，AgentState只能保存agent.invoke里面的messages信息
# 我们可以继承AgentState来保存我们自定义的字段
class CustomAgentState(AgentState):  # [!code highlight]
    user_id: str  # [!code highlight]
    preferences: dict  # [!code highlight]

# 修剪消息
# @before_model 是 LangChain 中用于在每次模型调用前执行自定义逻辑的装饰器，属于 Agent 中间件（Middleware）体系的一部分。
# 它让你能够在模型接收到输入之前，对 ModelRequest 或 AgentState 进行修改、检查或注入额外信息，从而影响模型的最终输入。
@before_model
def trim_messages(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
    """Keep only the last few messages to fit context window."""
    messages = state["messages"]

    if len(messages) <= 3:
        return None  # No changes needed

    print("----修剪消息----")
    first_msg = messages[0]
    recent_messages = messages[-3:] if len(messages) % 2 == 0 else messages[-4:]
    new_messages = [first_msg] + recent_messages

    # 删除所有消息，并将新的消息作为完整消息，重置对话
    return {
        "messages": [
            RemoveMessage(id=REMOVE_ALL_MESSAGES),
            *new_messages
        ]
    }

# 短期记忆 需要在创建代理时指定一个 checkpointer，同时在invoke中添加configurable，指定thread_id
agent = create_agent(
    model=basic_model,
    # system_prompt=system_prompt,
    tools=[calculator],
    middleware=[dynamic_model_selection, user_role_prompt, summarization],
    # response_format=toolStrategy  # 结构化输出

    checkpointer=InMemorySaver()  # 短期记忆
)

# 4. 调用 Agent
# context会传递给ModelRequest里面
response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": '''青岛的天气是什么并且提供最近几天的天气'''
            }
        ],
        "user_id": "1", # CustomAgentState接收
        "preferences": {"theme": "dark"} # CustomAgentState接收
    },
    {"configurable": {"thread_id": "1"}},
    context={"user_role": "expert"},

)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "刚才的问题是什么"}]},
    {"configurable": {"thread_id": "1"}},
    context={"user_role": "expert"},
)

# for chunk in agent.stream({
#     "messages": [{"role": "user", "content": "刚才的问题是什么"}]
# }, {"configurable": {"thread_id": "1"}}, context = {"user_role": "expert"}, stream_mode="values"):
#     # 每个块包含该时间点的完整状态
#     print(chunk)
#     latest_message = chunk["messages"][-1]
#     print(latest_message)
#     if latest_message.content:
#         print(f"智能体：{latest_message.content}")
#     elif latest_message.tool_calls:
#         print(f"正在调用工具：{[tc['name'] for tc in latest_message.tool_calls]}")


# print(response)
print(response["messages"][-1].content)


# 长期记忆
# 记录token
# 流式输出
# 上下文压缩
# MCP
# Skills
# 自定义代理记忆
# 多模态