from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
#used with chains 

load_dotenv()

#prompt template creation with template and input variables
template=PromptTemplate(
    template="""
You are an AI assistant helping {user_name}.
Your main task is {task}.
Provide clear """,
input_variables=['user_name','task'],
validate_template=True#check if all dynamic variables are available inisde the input variables
)


#storing the template
template.save('template.json')

#loading the template
template=load_prompt('template.json')

#giving dynamic varibale values
prompt=template.invoke({
    'user_name':"raju",
    "task":"washing"
})

print(template)

llm = ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

response = llm.invoke(prompt)

print(response.content)