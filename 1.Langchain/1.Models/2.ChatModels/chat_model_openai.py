from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

#add OPENAI_API_KEY IN .env
load_dotenv()

model=ChatOpenAI(model="gpt-4",temperature=0,max_completion_tokens=100)

result=model.invoke("Hi, How are you?")

print(result)
print(result.content)
