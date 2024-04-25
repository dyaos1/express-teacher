# create the chroma client
import dotenv, os
import chromadb
from chromadb.config import Settings

from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain


def history_aware_getter(question, history):
    # client
    client = chromadb.HttpClient(host="chroma", port=8000, settings=Settings(allow_reset=True))


    # embedding function
    dotenv.load_dotenv()
    embedding_function = OpenAIEmbeddings(api_key=os.getenv('API_KEY'))


    # llm
    llm = ChatOpenAI(api_key=os.getenv('API_KEY'))

    # chroma instance
    db = Chroma(
        client=client,
        collection_name="test_col",
        embedding_function=embedding_function,
    )

    # retrieval chain
    from langchain.chains import create_retrieval_chain, create_history_aware_retriever

    retriever = db.as_retriever()

    # history
    history_system_prompt = """Given a chat history and the latest user question \
        which might reference context in the chat history, formulate a standalone question \
        which can be understood without the chat history. Do NOT answer the question, \
        just reformulate it if needed and otherwise return it as is."""
    
    history_prompt = ChatPromptTemplate.from_messages([
        ("system", history_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ])

    history_retrieval_chain = create_history_aware_retriever(
        llm, retriever, history_prompt
    )

    
    qna_system_prompt = """You are an assistant for question-answering tasks. \
        Use the following pieces of retrieved context to answer the question. \
        If you don't know the answer, just say that you don't know. \
        Use three sentences maximum and keep the answer concise.\

        {context}"""
    
    qna_prompt = ChatPromptTemplate.from_messages([
        ("system", qna_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])
    qustion_answer_chain = create_stuff_documents_chain(llm, qna_prompt)

    rag_chain = create_retrieval_chain(history_retrieval_chain, qustion_answer_chain)


    from langchain_core.messages import HumanMessage

    chat_history = []

    for i in history:
        if i.type == 'client':
            chat_history.extend([HumanMessage(content=i.text)])
        if i.type == 'server':
            chat_history.extend([i.text])

    print(chat_history)
    
    the_answer = rag_chain.invoke({"input": question, "chat_history": chat_history})

    # question = "What is middleware?"
    # print(f"question: {question}")
    # ai_msg_1 = rag_chain.invoke({"input": question, "chat_history": chat_history})
    # print("answer: ", ai_msg_1["answer"])
    # chat_history.extend([HumanMessage(content=question), ai_msg_1["answer"]])
    
    # second_question = "방금 한 말 한국어로 다시 설명해줄래??"
    # print(f"question: {second_question}")
    # ai_msg_2 = rag_chain.invoke({"input": second_question, "chat_history": chat_history})
    # print("answer: ", ai_msg_2["answer"])

    # print(chat_history)

    # return ai_msg_2["answer"]

    return the_answer["answer"]

if __name__ == "__main__":
    history_aware_getter()
    