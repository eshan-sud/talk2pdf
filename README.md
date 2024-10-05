# Talk2PDFs - Website Chatbot

**Talk2PDFs** is a web application that lets users interact with PDF documents through a chatbot. Users can upload PDFs or provide URLs, and the chatbot will use the extracted content to answer questions.

## Technologies Used

- **Python**
- **Streamlit** - For the web interface.
- **Ollama** - Using the `llama3.2` model for language processing.
- **Visual Studio Build Tools** - Required for compiling dependencies like ChromaDB.

  1. Download and install Visual Studio Build Tools.
  2. During installation, make sure to select the **C++ build tools** workload.
  3. After installation, use pip to install ChromaDB

## Key Features

- **PDF Upload/URL Input:** Upload PDFs or provide URLs to process and extract text.
- **Text Extraction:** Extracts and processes text from PDFs for interaction.
- **Chatbot Interaction:** Ask questions related to the uploaded PDFs and get responses.
- **Text Preview:** View a snippet of the extracted text before asking questions.
- **Real-Time Responses:** Quickly get answers based on the content of the documents.
- **Integration with Vector Database:** Uses ChromaDB for efficient document retrieval.
- **Session Memory:** The chatbot retains previous interactions during a session for continuity.
- **Chat History:** Keeps a log of the session’s conversations.

## Setup

### Using setup.py

You can set up the project using the provided `setup.py` file. This will automatically install the required dependencies listed in `requirements.txt`.

1. Make sure you have a `requirements.txt` file with the necessary packages.
2. Run the following command to install the package:

### Manual Setup

If you prefer to set up manually:

1. Install Streamlit, Langchain, Langchain Community and ChromaDB:

   ```bash
   pip install streamlit langchain langchain_community chromadb
   ```

2. Running:

   ```bash
   streamlit run application.py
   ```

3. For running Ollama (LLM):

   ```bash
   ollama run llama3.2
   ```

## For Developers

### Virtual Environment Setup:

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On Windows:

```bash
source venv/bin/activate
```
