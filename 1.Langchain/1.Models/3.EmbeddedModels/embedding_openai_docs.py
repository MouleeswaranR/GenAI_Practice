from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)
documents=[
    "Dhoni is my favourite player",
    "Kohli is my 2nd favourite"
]

result=embeddings.embed_documents(documents)

print(str(result))