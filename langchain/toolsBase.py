
from langchain_core.tools import BaseTool
from langchain.tools import tool, ToolRuntime
from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated, Type, Any



class MyAgentInput(BaseModel):
    query: str = Field(description="需要查询的城市名称，必填")
    dateNum: str = Field(description="查询未来几天的天气，如果查询未来三天的天气，需要传输3")
    runtime: ToolRuntime

    model_config = ConfigDict(arbitrary_types_allowed=True)


class MyAgentTool(BaseTool):
    name: str =  "my_agent_tool"
    description: str = '''
    查询城市的天气
    
    **使用指南**
    1.根据用户的问题，得到城市名称，放入 query 中
    
    2.如果要未来几天的数据，需要将天数放到dateNum，如果未指定天数，那么就查询3天的天气
    
    3.如果获取不到城市名称，那么就不要进行检索天气，就按照正常方式进行
    
    4.如果用户问题和天气无关，也不执行检索天气，就按照正常方式进行
    '''
    args_schema: Type[BaseModel] = MyAgentInput

    def __init__(self):
        print("调用查询天气")
        super().__init__()

    def _run(self, query: str, dateNum: str, runtime: ToolRuntime) -> str:
        try:
            # runtime存放着 context state  config  tool_call_id
            # 其中 context 数据来自 invoke 或 stream 调用时的 context 参数
            # agent.invoke(
            #     {"messages": [{"role": "user", "content": "北京天气"}]},
            #     context={"user_role": "expert"}  # 这里传入的数据会出现在 runtime.context
            # )
            # messages = runtime.state["messages"]
            # 使用 存储（store） 访问跨对话的持久数据。通过 runtime.store 访问存储
            # store = runtime.store
            # user_info = store.get(("users",), 1)
            # print("user_info:" + user_info)

            # a = 1/0
            if dateNum:
                print("执行天气检索，查询天数：" + dateNum)
                return f"未来{dateNum}天天气，分别是，下雨，72°F，阴天，44°F，晴朗，88°F"
            else:
                print("执行天气检索，获取到的天气为：" + query)
                return f"{query} 的天气：晴朗，72°F"
        except Exception as e:
            # 向模型返回自定义错误消息
            print(e)
            return "检索不可用，请稍后再试."

    def _arun(self, query: str, **kwargs: Any) -> str:
        return f"{query} 的天气：晴朗，72°F"

class ContactInfo(BaseModel):
    city: str