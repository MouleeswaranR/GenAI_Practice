from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
import os

load_dotenv()

model=ChatOpenAI(
     model="meta-llama/llama-3-8b-instruct",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)


prompt=PromptTemplate(
    template='Write a summary about following poem - \n{poem}',
    input_variables=['poem']
)

parser=StrOutputParser()


loader=TextLoader('cricket.txt',encoding="utf-8")

docs=loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)


chain=prompt|model|parser

result=chain.invoke({'poem':docs[0].page_content})


print(result)

