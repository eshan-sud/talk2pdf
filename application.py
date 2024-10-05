# application.py

import streamlit as st
import util
from chatbot import create_chatbot_chain, get_chatbot_response

def file_uploader():
    uploaded_files = st.file_uploader("Upload PDFs", accept_multiple_files=True, type="pdf")
    if uploaded_files:
        with st.spinner('Extracting text from uploaded PDFs...'):
            corpus = ""
            for file in uploaded_files:
                corpus += util.extract_text_from_pdf(file)
            st.session_state['corpus'] = corpus
        st.success('Text extraction from uploaded PDFs completed!')

def url_input():
    pdf_url = st.text_input("Enter PDF URL")
    if pdf_url:
        with st.spinner('Extracting text from PDF URL...'):
            corpus = util.extract_text_from_url(pdf_url)
            st.session_state['corpus'] = corpus
        st.success('Text extraction from PDF URL completed!')

def init_sidebar():
    with st.sidebar.expander("About", expanded=True):
        st.title("Talk2PDFs")
        st.markdown("Upload PDFs or enter PDF URLs to interact with the chatbot.")        
        st.info("For any questions or issues, please reach out to me")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("[GitHub](https://github.com/eshan-sud)")
        with col2:
            st.markdown("[LinkedIn](https://www.linkedin.com/in/eshan-sud/)")
    st.sidebar.caption("© 2024 Eshan Sud. All rights reserved.")

def init_app():
    st.title("Talk to PDF with RAG Chatbot 🧠")
    st.markdown("### Upload PDFs or Provide URLs")
    st.caption("You can either upload files from your system or provide URLs to PDFs.")
    
    st.divider()

    # Add an option to toggle between inputs
    input_type = st.radio("Choose input type:", ("Upload PDFs", "Enter URLs"), horizontal=True)
    
    if input_type == "Upload PDFs":
        file_uploader()
    elif input_type == "Enter URLs":
        url_input()

    corpus = st.session_state.get('corpus', '')

    if corpus:
        with st.expander("Extracted Text Preview", expanded=False):
            st.text_area("Preview", value=corpus[:500], height=200, key='preview')

        # Initialize the chatbot with the corpus here
        if 'chatbot_chain' not in st.session_state:
            st.session_state['chatbot_chain'] = create_chatbot_chain()

    # Display chat history
    if 'chat_history' in st.session_state and st.session_state['chat_history']:
        for message in st.session_state['chat_history']:
            with st.chat_message(message["role"]):
                st.markdown(message["message"])

    question = st.text_input("Ask a question about the PDFs/URLs:")

    if st.button("Submit Question"):
        if corpus and question:
            # Store user message in chat history
            user_message = {"role": "user", "message": question}
            st.session_state['chat_history'].append(user_message)

            with st.spinner('Processing your question...'):
                response = get_chatbot_response(st.session_state['chatbot_chain'], question)
                if response:
                    # Store assistant response in chat history
                    chatbot_message = {"role": "assistant", "message": response}
                    st.session_state['chat_history'].append(chatbot_message)

                    st.success("Response received!")
                    st.write("**Response:**", response)
                else:
                    st.error("No response available.")
        else:
            st.error("Please upload PDFs or enter URLs first, and then ask a question.")

    if corpus:
        st.progress(100)

init_app()
init_sidebar()
