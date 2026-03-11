from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

parser=JsonOutputParser()

model=ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

template=PromptTemplate(
    template='Give me the name, age and city of M.S.Dhoni \n {format_instruction}',#format_instruction_format for output from llm(defaultly provided value from parser no need for user to invoke it )
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}#parser helps in creating value for format_instructions before runtime
)

prompt=template.format()


print(prompt)


chain=template|model|parser

result=chain.invoke({})#passing empty {} because there are no input_variables in template 

# parsed_result=parser.parse(result.content)#return dictionary
print(result)