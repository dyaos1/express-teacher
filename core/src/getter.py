# create the chroma client
import dotenv, os
import chromadb
from chromadb.config import Settings

from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain


def getter(question: str):
    # client
    client = chromadb.HttpClient(settings=Settings(allow_reset=True))


    # embedding function
    dotenv.load_dotenv()
    embedding_function = OpenAIEmbeddings(api_key=os.getenv('API_KEY'))


    # llm
    llm = ChatOpenAI(api_key=os.getenv('API_KEY'))


    # prompt template
    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

    <context>
    {context}
    </context>

    Question: {input}""")

    document_chain = create_stuff_documents_chain(llm, prompt)


    # chroma instance
    db = Chroma(
        client=client,
        collection_name="test_col",
        embedding_function=embedding_function,
    )

    # retrieval chain
    from langchain.chains import create_retrieval_chain 
    retriever = db.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)


    # response = retrieval_chain.invoke({"input": ""})
    response = retrieval_chain.invoke({"input": question})
    return response["answer"]
    