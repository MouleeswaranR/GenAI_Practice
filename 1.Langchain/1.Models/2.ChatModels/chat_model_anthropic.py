from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

#add ANTHROPIC_API_KEY to .env

load_dotenv()


model=ChatAnthropic(model='claude-3-5-sonnet-20241022')

result=model.invoke("Who is the first captain to win all 3 ICC Trophies")


print(result)

print(result.content)

