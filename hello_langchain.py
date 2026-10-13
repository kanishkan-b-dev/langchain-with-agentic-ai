from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from infomation import information, summary_template

load_dotenv()

def main():
    print("Hello from langchain!")

    summary_prompt_template = PromptTemplate(
        input_variables = ['information'], template = summary_template
    )

    llm = ChatOpenAI(temperature=0.6, model='gpt-4o-mini')
    chain = summary_prompt_template | llm
    response = chain.invoke(input={'information':information})
    print(response.content)

if __name__ == "__main__":
    main()
