#deepseek版本
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
import tools
from dotenv import load_dotenv
import os # 添加os模块用于加载环境变量
load_dotenv()
# 修正模型配置
model = OpenAIModel(
    "deepseek-reasoner",
    provider=OpenAIProvider(
        api_key=os.getenv('DS_API_KEY'), # 从环境变量加载API密钥
        base_url="https://api.deepseek.com"
    )
)
agent = Agent(
    model,
    system_prompt='你是windows平台脚本大师,可以灵活搭配cmd和python脚本指令去实现用户需求',
    tools=[
        tools.create_text_file,
        tools.create_python_file,
        tools.get_directory_structure,
        tools.rename_file,
        tools.execute_windows_command
        ] # tools用AI写就行了
)

def main():
    history = []
    while True:
        user_input = input("Input: ")
        resp = agent.run_sync(user_input,
                              message_history=history)
        history = list(resp.all_messages())
        print(resp.output)


if __name__ == "__main__":
    main()