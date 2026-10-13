import os
from pydantic import BaseModel, Field
from typing import List
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

class Source(BaseModel):
    '''
    Schema for a source used by the agent.
    '''

    url:str = Field(description="The URL for the source")

class AgentResponse(BaseModel):
    '''
    Schema for agent response with answer and sources.
    '''

    answer:str =  Field(description="The Agent's answer to the query")
    sources: List[Source] = Field(default_factory=list, description="List of sources used to generate the Object.")


llm = ChatOpenAI()
tool=[TavilySearch()]
agent = create_agent(model=llm, tools=tool, response_format=AgentResponse)


def main():
    print("Hello from Search Agent!")
    result = agent.invoke({"messages": HumanMessage(content="What is the wheather today in Chennai")})
    print(result)
    # result = agent.invoke({
    # "messages": [
    #     HumanMessage(content="Search AIML Job posting for 2 years of experience in India, mostly see for MNCs and let me know")
    #     ]
    # })

    # for message in result["messages"]:
    #     print(type(message).__name__, ":", message.content)

if __name__ == "__main__":
    main()
