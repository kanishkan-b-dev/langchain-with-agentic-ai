import os
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from tavily import TavilyClient


load_dotenv()

tavily = TavilyClient()

@tool
def search(user_query: str) -> str:
    '''
        Tool used to search over the internet for answers
        Args:
            user_query: Here is where the user query will be, need to take this and search in internet.
        Retruns:
            The results fetched from the internet.
    '''

    print(f"processing user query {user_query} !!!")
    return tavily.search(query=user_query)

llm = ChatOpenAI()
tool=[search]
agent = create_agent(model=llm, tools=tool)

def main():
    print("Hello from Search Agent!")
    # result = agent.invoke({"messages": HumanMessage(content="What is the wheather today in Chennai")})
    # print(result)
    result = agent.invoke({
    "messages": [
        HumanMessage(content="Search AIML Job posting for 2 years of experience and let me know")
        ]
    })

    for message in result["messages"]:
        print(type(message).__name__, ":", message.content)

if __name__ == "__main__":
    main()
