# from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# llm=HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation"
# )

# model=ChatHuggingFace(llm=llm)

model=ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

template1=PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=['topic']
)

template2=PromptTemplate(
    template="write a 5 line summary on the following text. /n {text}",
    input_variables=['text']
)


parser=StrOutputParser()

#pipeline chain
chain=template1 | model | parser | template2 | model | parser

#sending input for template1 in pipeline chain
result=chain.invoke({'topic':'blackhole'})

print(result)
