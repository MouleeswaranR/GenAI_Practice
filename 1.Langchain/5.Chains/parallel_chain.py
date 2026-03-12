from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
import os

load_dotenv()

model1=ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

model2=ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

prompt1=PromptTemplate(
    template='Generate a short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2=PromptTemplate(
    template='Generate 5 short questions answers from the following text \n {text} ',
    input_variables=['text']
)

prompt3=PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz} ',
    input_variables=['notes','quiz']
)

parser=StrOutputParser()

#parallel chain 

parallel_chain=RunnableParallel({
    'notes': prompt1|model1|parser,
    'quiz':prompt2|model2|parser
}
)

#outputs from parallel chain is merged using this chain
merge_chain=prompt3|model1|parser

chain=parallel_chain|merge_chain

text="""
Cricket is one of the most popular sports in the world.
It is played between two teams, each with eleven players.
The game is played on a large field with a pitch in the center.
One team bats while the other team bowls and fields.
The batting team tries to score runs by hitting the ball.
The bowling team tries to get the batsmen out.
Cricket includes different formats like Test matches, One Day Internationals, and T20 games.
Many countries such as India, Australia, and England are famous for their strong cricket teams.
Major tournaments like the ICC Cricket World Cup attract millions of fans worldwide.
Cricket is loved for its excitement, teamwork, and competitive spirit.
"""

result=chain.invoke({'text':text})

print(result)

chain.get_graph().draw_ascii()


