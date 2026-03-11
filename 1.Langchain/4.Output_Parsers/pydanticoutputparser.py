from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()



model=ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

class Person(BaseModel):

    name:str=Field(description="Name of person")
    age:int=Field(gt=18,description="Age of the person")
    city:str=Field(description='Name of the ciy the person belong to')

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template='Generate the name,age and city of M.S.Dhoni {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


# prompt=template.invoke({'place':'indian'})

# print(prompt)

# result=model.invoke(prompt)

# final_result=parser.parse(result.content)

chain=template|model|parser

final_result=chain.invoke({'place':'indian'})

print(final_result)