from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

documents=[
    "Dhoni is my favourite player",
    "Kohli is my 2nd favourite",
    "Dhoni is my favourite player",
    "Kohli is my 2nd favourite player"
]

query='tell about kohli'

doc_embeddings=embedding.embed_documents(documents)

query_embedding=embedding.embed_query(query)

scores=cosine_similarity([query_embedding],doc_embeddings)[0]

index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(documents[index])
print("similarity score is:", score)

