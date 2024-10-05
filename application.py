# application.py

import streamlit as st
import util
from chatbot import create_chatbot_chain, get_chatbot_response

def file_uploader():
    """Handles PDF file upload and text extraction."""
    uploaded_files = st.file_uploader("Upload PDFs", accept_multiple_files=True, type="pdf")
    if uploaded_files:
        with st.spinner('Extracting text from uploaded PDFs...'):
            corpus = "".join(util.extract_text_from_pdf(file) for file in uploaded_files)
            st.session_state['corpus'] = corpus
            st.write(f"Extracted {len(corpus)} characters from the PDFs.")
        st.success('Text extraction from uploaded PDFs completed!')

def url_input():
    """Handles URL input and text extraction."""
    pdf_url = st.text_input("Enter PDF URL")
    if pdf_url:
        with st.spinner('Extracting text from PDF URL...'):
            corpus = util.extract_text_from_url(pdf_url)
            st.session_state['corpus'] = corpus
            st.write(f"Extracted {len(corpus)} characters from the URLs.")
        st.success('Text extraction from PDF URL completed!')

def init_sidebar():
    """Initializes the sidebar with information and links."""
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

def display_extracted_text(corpus):
    """Displays the extracted text preview."""
    with st.expander("Extracted Text Preview", expanded=False):
        st.text_area("Preview", value=corpus[:500], height=200, key='preview')

def handle_chat(corpus):
    """Handles user questions and chatbot responses."""
    question = st.text_input("Ask a question about the PDFs/URLs:", key='question_input')
    if st.button("Submit Question"):
        if corpus and question:
            user_message = {"role": "user", "message": question}
            st.session_state.setdefault('chat_history', []).append(user_message)

            with st.spinner('Processing your question...'):
                response = get_chatbot_response(st.session_state['chatbot_chain'], question)
                if response:
                    chatbot_message = {"role": "assistant", "message": response}
                    st.session_state['chat_history'].append(chatbot_message)
                    st.success("Response received!")
                    st.write("**Response:**", response)
                else:
                    st.error("No response available.")
        else:
            st.error("Please upload PDFs or enter URLs first, and then ask a question.")

def display_chat_history():
    """Displays the chat history."""
    if 'chat_history' in st.session_state and st.session_state['chat_history']:
        for message in st.session_state['chat_history']:
            with st.chat_message(message["role"]):
                st.markdown(message["message"])
    else:
        st.write("No chat history available.")

def init_app():
    """Initializes the Streamlit app."""
    st.set_page_config(page_title="Talk2PDFs - Eshan Sud")
    st.title("Talk to PDF with RAG Chatbot 🧠")
    st.markdown("### Upload PDFs or Provide URLs")
    st.caption("You can either upload files from your system or provide URLs to PDFs.")
    st.divider()

    # Check if necessary session state variables are initialized
    st.session_state.setdefault('corpus', '')

    # Add an option to toggle between inputs
    input_type = st.radio("Choose input type:", ("Upload PDFs", "Enter URLs"), horizontal=True)
    if input_type == "Upload PDFs":
        file_uploader()
    elif input_type == "Enter URLs":
        url_input()

    corpus = st.session_state.get('corpus', '')
    if corpus:
        display_extracted_text(corpus)

        if 'chatbot_chain' not in st.session_state:
            st.session_state['chatbot_chain'] = create_chatbot_chain()  # Ensure this is called after initialization

    # Create tabs for current chat and chat history
    tabs = st.tabs(["Chat", "History"])
    with tabs[0]:  # Chat Tab
        handle_chat(corpus)

    with tabs[1]:  # History Tab
        display_chat_history()

    if corpus:
        st.progress(100)

if __name__ == "__main__":
    init_app()
    init_sidebar()