from pathlib import Path
from deepagents import create_deep_agent
from langchain_openai import ChatOpenAI
from deepagents.backends import FilesystemBackend

# 1. 路径标准化处理
current_root = Path(__file__).parent.resolve()
print(current_root)
skills_dir = (current_root / "skills").as_posix() # 统一为正斜杠 /

# 2. 初始化 Backend
backend = FilesystemBackend(root_dir=str(current_root), virtual_mode=True)

# 3. 创建 Agent
agent = create_deep_agent(
    model=ChatOpenAI(
        model='deepseek-v4-pro', # V3 在工具调用上比 R1 更稳
        base_url='https://api.deepseek.com',
        api_key='sk-41537a9660f74513b87c2ca5c36165d6',
        extra_body={"thinking": {"type": "disabled"}}
    ),
    backend=backend,
    skills=[skills_dir], # 注入技能路径
    system_prompt="你是一个办公助手。必须根据用户需求调用对应的工具完成任务。"
)

# result = agent.invoke({
#     "messages": [
#         {"role": "user", "content": "帮我只做一个关于环境保护的word"}
#     ]
# })
# print(result["messages"][-1]["content"])

if __name__ == "__main__":
    allContent = ''

    inputs = {"messages": [{"role": "user", "content": "帮我只做一个关于环境保护的word"}]}

    for chunk in agent.stream(inputs, config={"configurable": {"thread_id": "job_01"}}):
        # 监控：是否加载成功
        if 'SkillsMiddleware.before_agent' in chunk:
            count = len(chunk['SkillsMiddleware.before_agent'].get('skills_metadata', []))
            print(f"📊 状态: 已加载 {count} 个技能")

        # 监控：正在做什么
        print(f"chunk:{chunk}")

        if 'model' in chunk:
            allContent = allContent + chunk['model']['messages'][0].content
            msg = chunk['model']['messages'][0]
            print(msg)
            if msg.tool_calls:
                # 只打印动作名称，不打印那一长串内容
                print(f"🤔 动作: 正在调用 [{msg.tool_calls[0]['name']}]...")

        # 结果：最终回答
        if 'agent' in chunk:
            print(f"\n🎯 结果:\n{chunk['agent']['messages'][-1].content}")

    print(f"count:{allContent}")



