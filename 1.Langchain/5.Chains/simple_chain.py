from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

prompt=PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model=ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

parser=StrOutputParser()


chain=prompt|model|parser

result=chain.invoke({'topic':'cricket'})

chain.get_graph().print_ascii()#print working flow  map of the chain

print(result)