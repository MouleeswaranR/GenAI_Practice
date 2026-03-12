from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
import os

load_dotenv()

model=ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

parser=StrOutputParser()

class Feedback(BaseModel):

    sentiment:Literal['positive','negative']=Field(description="Give the sentiment of the feedback")

parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser2.get_format_instructions()}
)

#classifies the given feedback as positive or negative
classifier_chain=prompt1|model|parser2

# result=classifier_chain.invoke({'feedback':"this is a terrible product"}).sentiment

# print(result)

#for positive response
prompt2=PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

#for negative response
prompt3=PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)


#conditional chain
branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive',prompt2|model|parser),#x ix the output from classifier_chain
    (lambda x:x.sentiment=='negative',prompt3|model|parser),
    RunnableLambda(lambda x:"could not find sentiment")
)

chain=classifier_chain|branch_chain

result=chain.invoke({'feedback':"this is a terrible phone"})

print(result)

chain.get_graph().print_ascii()

