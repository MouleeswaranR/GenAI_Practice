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
json_schema={
  "title": "review",
  "description": "Schema for analyzing a product review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Write down all key themes discussed in the review"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["positive", "negative", "neutral"],
      "description": "Return sentiment of review: negative, positive, or neutral"
    },
    "pros": {
      "type": ["array","null"],
      "items": { "type": "string" },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array","null"],
      "items": { "type": "string" },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": "string",
      "description": "Write name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}


structured_model=model.with_structured_output(json_schema)

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




