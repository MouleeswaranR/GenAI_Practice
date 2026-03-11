from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage


chat_template=ChatPromptTemplate([ #also use ChatPromptTemplate.from_messages same output as ChatPromptTemplate
    ('system','You are a helpful {domain} expert'),
    ('human','Explain in short terms , what is {topic}')
    # SystemMessage(content='You are a helpful {domain} expert'),
    # HumanMessage(content='Explain in short terms , hat is {topic}')
])

prompt = chat_template.invoke({
    'domain':'cricket',
    'topic':'LBW'
})

print(prompt)