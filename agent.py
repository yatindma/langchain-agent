# agent.py
from langchain.agents import AgentExecutor, create_react_agent
from tools import KeywordSearchTool, Calculator
from langchain_openai import OpenAI
from langchain import hub


def initialize_agent():
    prompt = hub.pull("hwchase17/react")
    llm = OpenAI(temperature=0)
    tools = [KeywordSearchTool(), Calculator()]
    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)

def run_agent(agent, input_query):
    # print("Running agent with query:", input_query)
    return agent.invoke({'input': input_query})
