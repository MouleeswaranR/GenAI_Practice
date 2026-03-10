from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

#add GOOGLE_API_KEY to .env
load_dotenv()


model=ChatGoogleGenerativeAI(model='gemini-2.0-flash')

result=model.invoke("Who is the first captain to win all 3 ICC Trophies")

print(result.content)