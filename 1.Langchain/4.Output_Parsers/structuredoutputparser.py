from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsing import StructuredOutputParser, ResponseSchema
#StructuredOutputParser depreceated in latest version

load_dotenv()


model=ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

schema=[
    ResponseSchema(name='fact_1',description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2',description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3',description='Fact 3 about the topic'),
]

parser=StructuredOutputParser.from_response_schema(schema)

template=PromptTemplate(
    template='Give 3 facts about {topic}\n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt=template.invoke({'topic':'blackhole'})

result=model.invoke(prompt)

final_result=parser.parse(result.content)

print(final_result)