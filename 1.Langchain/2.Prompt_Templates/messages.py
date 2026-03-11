from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model=ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

#storing chat history with formatted manner 
messages=[
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="tell me about langchain")
]

result=model.invoke(messages)

#appending output from LLM
messages.append(AIMessage(content=result.content))

print(result.content)


