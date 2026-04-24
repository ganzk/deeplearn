
from langchain.agents import create_agent


from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.tools import tool


@tool
def multiply(a: int, b: int) -> int:
    """将两个整数相乘。"""
    return a * b

# 配置 DeepSeek 的 API 信息
llm = ChatOpenAI(
    model="deepseek-chat",  # 或使用 "deepseek-reasoner"（推理模型）
    openai_api_key="sk-9057255f494b4076b774b1a617491e55",  # 你的 DeepSeek API Key
    openai_api_base="https://api.deepseek.com/v1",  # DeepSeek 的 API 地址
    temperature=0.7,
    max_tokens=1024
)

agent = create_agent(
    model = llm,
    system_prompt= '''你现在是一名专业的A股投资内容解读专家，
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
)

# 4. 调用 Agent
response = agent.invoke({
    "messages": [{"role": "user", "content": ''''''}]
})

print(response["messages"][-1].content)