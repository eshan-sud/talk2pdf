# chatbot.py

import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.llms.ollama import Ollama
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# Ensure required directories exist
if not os.path.exists("pdfFiles"):
    os.makedirs("pdfFiles")
if not os.path.exists("vectorDB"):
    os.makedirs("vectorDB")

# Initialize session state variables
if 'template' not in st.session_state:
    st.session_state.template = """
You are a knowledgeable chatbot, here to help with questions of the user. Your tone should be professional and informative.
If you cannot find relevant information in the PDFs, please respond with: "No relevant information in the PDFs for your question."
Context: {context}
History: {history}
User: {query}
Chatbot:
    """

if 'prompt' not in st.session_state:
    st.session_state.prompt = PromptTemplate(
        input_variables=["history", "context", "query"],
        template=st.session_state.template,
    )


if 'memory' not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="history",
        return_messages=True,
        input_key="query",
    )


if 'vectorstore' not in st.session_state:
    st.session_state.vectorstore = Chroma(
        persist_directory='vectorDB',
        embedding_function=OllamaEmbeddings(
            base_url='http://localhost:11434',
            model="llama3.2")
        )

if 'llm' not in st.session_state:
    st.session_state.llm = Ollama(
        base_url="http://localhost:11434",
        model="llama3.2",
        verbose=True,
        callback_manager = CallbackManager(
           [StreamingStdOutCallbackHandler()]
        ),
    )

if 'chat_history' not in st.session_state:
   st.session_state.chat_history = []

# Function to create the chatbot chain
def create_chatbot_chain():
    if 'llm' not in st.session_state:
        st.session_state.llm = Ollama(
            base_url="http://localhost:11434",
            model="llama3.2",
            verbose=True,
            callback_manager=CallbackManager(
                [StreamingStdOutCallbackHandler()]
            ),
        )

    if 'vectorstore' not in st.session_state:
        st.session_state.vectorstore = Chroma(
            persist_directory='vectorDB',
            embedding_function=OllamaEmbeddings(
                base_url='http://localhost:11434',
                model="llama3.2")
        )

    retriever = st.session_state.vectorstore.as_retriever()
    return RetrievalQA.from_chain_type(
        llm=st.session_state.llm,
        chain_type="stuff",
        retriever=retriever,
        verbose=True,
        memory=st.session_state.memory
    )

# Function to get chatbot response
def get_chatbot_response(chatbot_chain, question):
    response = chatbot_chain({"query": question})
    if 'no information' in response['result'].lower() or 'not found' in response['result'].lower():
        return "No relevant information in the PDFs for your question."
    return response['result']
