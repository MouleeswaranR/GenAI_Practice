from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

model=ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

prompt1=PromptTemplate(
    template='Generate a detailed repost on {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Generate a 5 point summary on following text {text}',
    input_variables=['text']
)

parser=StrOutputParser()

#taking output from prompt template , giving it to llm and parsing output from llm , again passing it to prompt2 and llm and getting output
chain=prompt1 | model | parser | prompt2 | model |parser

result=chain.invoke({'topic':"cricket"})

print(result)


chain.get_graph().print_ascii()