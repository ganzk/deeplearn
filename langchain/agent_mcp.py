from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

from agent_model import basic_model, advanced_model

client = MultiServerMCPClient(
    {
        "math": {
            "transport": "stdio",  # 本地子进程通信
            "command": "python",
            # 您的 math_server.py 文件的绝对路径
            "args": ["/path/to/math_server.py"],
        },
        "weather": {
            "transport": "streamable_http",  # 基于 HTTP 的远程服务器
            # 确保您在 8000 端口启动了您的天气服务器
            "url": "http://localhost:8000/mcp",
        }
    }
)

async def agentMcp ():
    tools = await client.get_tools()
    agent = create_agent(
        basic_model,
        tools
    )
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )
    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
    )