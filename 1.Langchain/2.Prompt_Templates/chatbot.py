from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

model=ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL"),
    max_completion_tokens=40
)

#store chat history for llm to remember previous chat for reasoning

# chat_history=[]

#not a efficient one because LLM does not know which message is from it or from user

#Efficient one is dicionary structure using langchain messages
chat_history=[
    SystemMessage(content="You are a helpful assistant")
]

while True:
    user_input=input('User: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)


print(chat_history)




