from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from langchain.toolsBase import MyAgentTool


# 配置 DeepSeek 的 API 信息
basic_model = ChatOpenAI(
    model="deepseek-chat",  # 或使用 "deepseek-reasoner"（推理模型）
    openai_api_key="sk-9057255f494b4076b774b1a617491e55",  # 你的 DeepSeek API Key
    openai_api_base="https://api.deepseek.com/v1",  # DeepSeek 的 API 地址
    temperature=0.7,
    max_tokens=1024
)

# 工具-继承BaseTool方式创建
calculator = MyAgentTool()

agent = create_agent(
    model=basic_model,
    tools=[calculator],
)

# 代理进度  使用stream_mode="updates" 这会在每个代理步骤后发出一个事件，返回结果如下：
# step: model
# content: [{'type': 'text', 'text': '我来帮您查询青岛的天气情况。'}, {'type': 'tool_call', 'name': 'my_agent_tool', 'args': {'query': '青岛', 'dateNum': '3'}, 'id': 'call_00_IMJNtXYGANWKWa6UpIemaNWJ'}]
# 执行天气检索，查询天数：3
# step: tools
# content: [{'type': 'text', 'text': '未来3天天气，分别是，下雨，72°F，阴天，44°F，晴朗，88°F'}]
# step: model
# content: [{'type': 'text', 'text': '根据查询结果，青岛未来3天的天气情况如下：\n\n**第1天**：下雨，气温72°F（约22°C）\n**第2天**：阴天，气温44°F（约7°C）\n**第3天**：晴朗，气温88°F（约31°C）\n\n青岛的天气变化比较大，从第一天的下雨到第三天的晴朗，气温也有较大波动。建议您根据出行时间准备相应的衣物和雨具。'}]
# for chunk in agent.stream(  # [!code highlight]
#     {"messages": [{"role": "user", "content": "青岛的天气是什么？"}], "user_id": "1"},
#     stream_mode="updates",
# ):
#     for step, data in chunk.items():
#         print(f"step: {step}")
#         print(f"content: {data['messages'][-1].content_blocks}")


# 要在 LLM 生成令牌时流式传输它们，请使用 stream_mode="messages"。
for token, metadata in agent.stream(  # [!code highlight]
    {"messages": [{"role": "user", "content": "青岛的天气是什么?"}], "uesr_id": "1"},
    context={"user_id": "123", "request_id": "abc"},
    stream_mode="messages",
):
    print(f"node: {metadata['langgraph_node']}")
    print(f"content: {token.content_blocks}")
    print("\n")


# 可以多种模式
# for stream_mode, chunk in agent.stream(  # [!code highlight]
#     {"messages": [{"role": "user", "content": "青岛的天气是什么?"}], "uesr_id": "1"},
#     stream_mode=["updates", "custom"]
# ):
#     print(f"stream_mode: {stream_mode}")
#     print(f"content: {chunk}")
#     print("\n")