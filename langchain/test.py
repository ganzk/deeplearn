
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
    system_prompt= ""
)