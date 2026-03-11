from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field

load_dotenv()

model=ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

#structure/schema

class Review(BaseModel):
    #Field-allows to add metadata about variable and it's data type
    key_themes: list[str]=Field(description="write down all key themes dicussed in the review")
    summary:str=Field(description="A brief summary of review")
    sentiment:Literal["positive","negative","neutral"]=Field(description="return sentiment of review either negative ,positive or neutral")
    pros:Optional[list[str]]=Field(description="Write down all the pros inside a list")
    cons:Optional[list[str]]=Field(description="Write down all the cons inside a list")
    name:Optional[str]=Field(description="Write name of the reviewer")

    #Annotated-helps in adding metadata about a varible with type
    #Literal-allows to give a list of options as type to a variable
    #Optional-makes the variable optional with its type
    # key_themes: Annotated[list[str],'write down all key themes dicussed in the review']
    # summary:Annotated[str,"A brief summary of review"]
    # sentiment:Annotated[Literal["positive","negative","neutral"],"return sentiment of review either negative ,positive or neutral" ]
    # pros:Annotated[Optional[list[str]],'Write down all the pros inside a list']
    # cons:Annotated[Optional[list[str]],'Write down all the cons inside a list']


structured_model=model.with_structured_output(Review)

result=structured_model.invoke("""
I recently purchased the Apple iPhone 15, and overall my experience has been very positive. The design feels premium and comfortable to hold, with a sleek finish that looks modern. The display is bright and sharp, making videos and photos look stunning. I especially liked how smooth the performance is when switching between apps. The camera quality is excellent and captures detailed photos even in low light.

Battery life is another strong point because it easily lasts through a full day of normal use. Charging is fairly quick, which is convenient when you’re in a hurry. The sound quality from the speakers is clear and loud enough for watching movies or listening to music. I also noticed that the phone stays cool even after extended use.

However, the price is quite high compared to many other smartphones with similar features. Some accessories also need to be purchased separately, which adds to the cost. Despite that, the overall build quality and performance make it feel like a reliable device.

In conclusion, the iPhone 15 is a powerful and stylish smartphone with great camera performance and smooth operation. While it may be expensive, it is a good option for users who want a premium mobile experience. I would recommend it to people who value quality and long-term performance in a smartphone.

                               by raju
                               """)

if isinstance(result, list):
    result = result[0]

print(type(result))
print(result)
# print(result['summary'])
# print(result['sentiment'])

#cons of TypedDict
#rigid structure-fixed
#no nested validation
#no runtime enforcement-At runtime, Python won’t throw an error if the model returns the wrong type.
#single structure limitation to the model-model can't handle multiple typeddict schmeas at once




