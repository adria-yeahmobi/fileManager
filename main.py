from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai import Agent

from dotenv import load_dotenv
import tools
import os

load_dotenv()
print("GEMINI_API_KEY:", os.getenv("GEMINI_API_KEY"))

model = GeminiModel("gemini-2.5-flash-preview-04-17")


agent = Agent(model,
              system_prompt="You are an experienced programmer",
              tools=[tools.read_file, tools.list_files, tools.rename_file])

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