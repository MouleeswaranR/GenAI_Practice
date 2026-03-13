from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path='books',#directory path of the documents
    glob="*.pdf",#what files needed to be loaded
    loader_cls=PyPDFLoader, #loader for the filed that needed to be loaded
)

docs=loader.lazy_load()#loads one document at a time


print(docs[0].metadata)