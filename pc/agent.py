from langchain.agents import create_agent
from langchain.agents.middleware import dynamic_prompt, ModelRequest

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.tools import tool

@dynamic_prompt
def user_role_prompt(request: ModelRequest) -> str:
    """根据用户角色生成系统提示。"""
    ## 还可以将传递的入参，拼接到提示词中去
    print("request.runtime.context:", request.runtime.context)
    user_role = request.runtime.context.get("user_role", "user")
    expert_prompt = '''你现在是一名专业的A股投资内容解读专家，
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

    essence_prompt = """
        Role： 你是一位拥有 20 年经验的资深价值投资分析师，擅长拆解巴菲特、芒格、塞斯·卡拉曼等大师的致股东信和投资演讲。你能够将晦涩的金融术语转化为常识，并洞察文字背后的底层逻辑。
    
        Task： 请帮我深度解读以下这段文字：
        {文章内容}
        
        Requirements：
        
        核心逻辑拆解： 这段话的核心论点是什么？作者试图解决什么投资问题？
        
        术语通俗化： 如果文中涉及晦涩的金融或商业术语（如：自由现金流折现、护城河、资本配置、安全边际等），请结合上下文用生活化的例子解释。
        
        洞察商业本质： 作者在这里揭示了什么样的商业模式、竞争优势或人性弱点？
        
        实战启发： 站在普通投资者的角度，这段话对我的投资心态或决策有什么具体的指导意义？
        
        Output Format： 请使用清晰的标题和分点陈述，避免大段堆砌文字。
    """

    if user_role == "expert":
        return expert_prompt
    elif user_role == "essence":
        return essence_prompt

    return expert_prompt

def King_agent(text:str, type:str):
    # 配置 DeepSeek 的 API 信息
    llm = ChatOpenAI(
        model="deepseek-chat",  # 或使用 "deepseek-reasoner"（推理模型）
        openai_api_key="sk-9057255f494b4076b774b1a617491e55",  # 你的 DeepSeek API Key
        openai_api_base="https://api.deepseek.com/v1",  # DeepSeek 的 API 地址
        temperature=0.7,
        max_tokens=1024
    )

    agent = create_agent(
        model=llm,
        middleware=[user_role_prompt]
    )

    # 4. 调用 Agent
    response = agent.invoke({
        "messages": [{"role": "user", "content": text}]
    },
    context={"user_role": type}
    )

    return response["messages"][-1].content


