import dotenv, os

import chromadb
from chromadb.config import Settings

from langchain_community.vectorstores.chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from sitelist import sitelist

import chromadb.utils.embedding_functions as embedding_functions


# chromadb client init
client = chromadb.HttpClient(settings=Settings(allow_reset=True))
client.reset()


# embedding function
dotenv.load_dotenv()
embedding_function = OpenAIEmbeddings(api_key=os.getenv("API_KEY"))
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_key=os.getenv("API_KEY"),
                model_name="text-embedding-ada-002"
            )


# sitelist
sitelist = sitelist()


for idx, val in enumerate(sitelist):
    loader = WebBaseLoader(val)
    data = loader.load()

    # split data to texts
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = (text_splitter.split_documents(data))

    # create collection
    collection = client.get_or_create_collection("test_col", embedding_function=openai_ef)

    for idx2, doc in enumerate(docs):
        collection.add(
            ids=["id:" + str(idx) + "-" + str(idx2)], metadatas=doc.metadata, documents=doc.page_content
        )
