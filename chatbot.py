# chatbot.py

# Available only for 24 hrs : 
# https://llama3-1.llamameta.net/*?Policy=eyJTdGF0ZW1lbnQiOlt7InVuaXF1ZV9oYXNoIjoiZzg3eDhid2E2bG00M2Y0bzJpOTM2N2dhIiwiUmVzb3VyY2UiOiJodHRwczpcL1wvbGxhbWEzLTEubGxhbWFtZXRhLm5ldFwvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcyNDkxNTAxOX19fV19&Signature=AwCCpIVwfpO-fdTJ7ZODpNrKiJcUOldKl7Ri6hCsvBiq1N-TPnGBt0%7EsUQC57PMdEZLaB6p8klXwydUwEuCtTMSn5icGrliMLcHCHqDoXeieEhUDCzZrA9MsiF2yc3-Rt6RFYrmNiwZwyWyxnCB0oWPiUCaWhZzBspCkTYmWnwqSUMyxX3CnLVxu7ySU0A7wcgYTZrbLVW9QpUkG953XrARnmkkRllhh18m6FyeANkU0%7EX0Qh2vixIl-VLU8L2xZzAb2Iypts-9VE8EsbaM7oiB3UtW8NuHEttLqi9DWPkS6lSR7QMIlXdGKauJCq6XVcwwgb6WQDk1%7EPsOqytaBLw__&Key-Pair-Id=K15QRJLYKIFSLZ&Download-Request-ID=532195952518142

from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import LlamaCpp
from langchain.document_loaders import TextLoader
from langchain.retrievers import TFIDFRetriever
from langchain.prompts import ChatPromptTemplate

# Initialize Llama model with the correct model path
llm = LlamaCpp(
    model_path="C:/Users/Eshan Sud/.llama/checkpoints/Prompt-Guard-86M/model.safetensors",
    tokenizer_path="C:/Users/Eshan Sud/.llama/checkpoints/Prompt-Guard-86M/tokenizer.json"
)

# Load embeddings
embeddings = HuggingFaceEmbeddings()

# Build the document store and retriever
def create_retriever(corpus):
    loader = TextLoader.from_text(corpus)
    documents = loader.load_and_split()
    faiss_index = FAISS.from_documents(documents, embeddings)
    retriever = TFIDFRetriever(index=faiss_index)
    return retriever

# Create the RAG chatbot chain
def create_chatbot_chain(corpus):
    retriever = create_retriever(corpus)
    chatbot_chain = ConversationalRetrievalChain(
        llm=llm, retriever=retriever, prompt_template=ChatPromptTemplate.default()
    )
    return chatbot_chain

# Function to generate a response
def get_chatbot_response(chatbot_chain, question):
    response = chatbot_chain.run(input_text=question)
    return response