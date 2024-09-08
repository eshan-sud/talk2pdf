# application.py
import streamlit as st
import util
from chatbot import create_chatbot_chain, get_chatbot_response

corpus = ""

def file_uploader():
    uploaded_files = st.file_uploader("Upload PDFs", accept_multiple_files=True, type="pdf")
    if uploaded_files:
        with st.spinner('Extracting text from uploaded PDFs...'):
            global corpus
            corpus += util.extract_text_from_pdf(uploaded_files)
        st.success('Text extraction from uploaded PDFs completed!')

def url_input():
    pdf_url = st.text_input("Enter PDF URL")
    if pdf_url:
        with st.spinner('Extracting text from PDF URL...'):
            global corpus
            corpus += util.extract_text_from_url(pdf_url)
        st.success('Text extraction from PDF URL completed!')

def init_sidebar():
    with st.sidebar.expander("About", expanded=True, icon="⚙️"):
        st.title("Talk2PDFs")
        st.markdown("Upload PDFs or enter PDF URLs to interact with the chatbot.")        
        st.info("For any questions or issues, please reach out to me")
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("GitHub", "https://github.com/eshan-sud")
        with col2:
            st.link_button("LinkedIn", "https://www.linkedin.com/in/eshan-sud/")
    st.sidebar.caption("© 2024 Eshan Sud. All rights reserved.")

def init_app():
    st.title("Talk to PDF with RAG Chatbot")
    st.header("Upload PDFs or Provide URLs")
    st.caption("You can either upload files from your system or provide URLs to PDFs.")
    st.divider()
    
    input_type = st.radio("Choose input type:", ("Upload PDFs", "Enter URLs"))
    if input_type == "Upload PDFs":
        file_uploader()
    elif input_type == "Enter URLs":
        url_input()

    if corpus:
        st.subheader("Extracted Text Preview")
        st.text_area("Text Preview", value=corpus[:500], height=200, key='preview')

        # Initialize the chatbot with the corpus
        chatbot_chain = create_chatbot_chain(corpus)  # Uncommented and added here

    question = st.text_input("Ask a question about the PDFs/URLs:")
    if st.button("Submit Question"):
        if corpus and question:
            with st.spinner('Processing your question...'):
                response = get_chatbot_response(chatbot_chain, question)  # Updated to use the real function
                if response:
                    st.success("Response received!")
                    st.write("Response:", response)
                else:
                    st.error("No response available.")
        else:
            st.error("Please upload PDFs or enter URLs first, and then ask a question.")
            
    if corpus:
        st.progress(100)

init_app()
init_sidebar()
