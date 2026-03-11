from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage,AIMessage


#chat template

chat_template=ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history') ,#previous messages passed to LLM 
    ('human','{query}')
])

#load chat history from txt file
chat_history=[]

# with open('chat_history.txt') as f:
#     chat_history.append(f.readlines())

chat_history = [
    HumanMessage(content="I want to request a refund for my order #12345."),
    AIMessage(content="Sure, can you tell me the reason for the refund?")
]
print(chat_history)


#create prompt
prompt=chat_template.invoke({
    'chat_history':chat_history,
    'query':HumanMessage(content='Where is my refund')}
    )

print(prompt)


