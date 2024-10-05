# Talk2PDFs - Website Chatbot

**Talk2PDFs** is a web application that allows users to interact with PDF documents through a chatbot interface. Users can upload PDFs or provide URLs to extract and process the content, which the chatbot uses to answer questions.

## Technologies Used

- Python
- Streamlit
- Ollama - llama3.2 model

  ```
  ollama run llama3.2
  ```

- Visual Studio Build Tools:

Download and install Visual Studio Build Tools.
During installation, make sure to select the C++ build tools workload.
Install Required Libraries:

Some packages that chromadb relies on might need additional C++ libraries. Ensure you have numpy, scipy, and pandas installed as they are commonly used with chromadb.
Install chromadb:

Use pip to install:
bash
Copy code
pip install chromadb

## Key Features

- **PDF Upload and URL Input:** Upload PDFs or provide URLs to extract text from documents.
- **Text Extraction:** Extracts and processes text from PDFs for interaction.
- **Interactive Chatbot:** Engage with a chatbot that answers questions based on the content of the PDFs.
- **Text Preview:** Provides a preview of the extracted text for user reference.
- **Real-Time Processing:** Efficiently handles and processes user queries with minimal latency.
- **Easy Setup:** Simple installation and setup process using Streamlit.
- **Integration with Vector Database:** Uses FAISS and HuggingFace embeddings for efficient document retrieval and response generation.
- **Session Memory:**

## Setup

1. Install Streamlit & Langchain & ChromaDB:

   ```bash
   pip install streamlit langchain chromadb
   ```

2. Running:
   ```
   streamlit run application.py
   ```

<!-- pip install torch fairscale fire blobfile -->
