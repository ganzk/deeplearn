from langchain_openai import ChatOpenAI

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