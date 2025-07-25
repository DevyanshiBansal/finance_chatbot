# RAG-based Financial Chatbot

This project features an intelligent financial chatbot designed to provide comprehensive and context-aware responses to financial queries. Leveraging the power of Retrieval-Augmented Generation (RAG) and an advanced agentic architecture, this chatbot integrates various tools and databases to deliver accurate and content-rich information.

## Features

* **Intelligent Financial Q&A:** Answers user queries related to finance with high accuracy and relevance.
* **Gemini 2.5 Flash Integration:** Powered by Google's fast and efficient Gemini 2.5 Flash LLM for robust language understanding and generation.
* **Retrieval-Augmented Generation (RAG):** Enhances response quality by retrieving relevant information from external knowledge bases before generating answers, reducing hallucinations and ensuring factual accuracy.
* **LangChain Orchestration:** Utilizes the LangChain framework to seamlessly connect the LLM with various tools, databases, and agents.
* **ChromaDB Vector Store:** Employs ChromaDB as the vector database for efficient storage and retrieval of financial documents and data embeddings.
* **HuggingFace Embeddings:** Uses a HuggingFace embedding model to convert text into dense vector representations for effective similarity search in ChromaDB.
* **DuckDuckGo Search Tool:** Integrates DuckDuckGo as an external search tool, allowing the agent to fetch real-time or broader financial information from the web when internal data is insufficient.
* **Autonomous Agent:** An intelligent agent orchestrates the interaction between the LLM, vector database, and search tool, determining the best course of action to answer complex queries.

## Technologies Used

* **Large Language Model:** Google Gemini 2.5 Flash
* **Orchestration Framework:** LangChain
* **Vector Database:** ChromaDB
* **Embedding Model:** HuggingFace (e.g., `sentence-transformers/all-MiniLM-L6-v2` or similar)
* **Search Tool:** DuckDuckGo Search API
* **Programming Language:** Python

## Architecture

The chatbot's architecture is built around LangChain's agentic capabilities, with RAG as a core component for enhanced information retrieval:

1.  **User Query:** The user submits a financial query.
2.  **LangChain Agent:** An intelligent agent (powered by Gemini 2.5 Flash) receives the query. This agent is designed to reason about the query and decide which tools or data sources are most appropriate.
3.  **Retrieval-Augmented Generation (RAG) Flow:**
    * **Embedding:** The user query is converted into a vector embedding using the HuggingFace embedding model.
    * **ChromaDB Search:** This embedding is used to perform a similarity search in ChromaDB, retrieving relevant financial documents or data chunks.
    * **Contextualization:** The retrieved information is provided as context to the Gemini 2.5 Flash LLM.
4.  **Tool Utilization (DuckDuckGo):** If the agent determines that the internal knowledge base is insufficient or if real-time information is needed, it can invoke the DuckDuckGo search tool to fetch external data.
5.  **Gemini 2.5 Flash Generation:** The Gemini 2.5 Flash model then generates a comprehensive and accurate response, leveraging both the internal retrieved documents and potentially the real-time search results.
6.  **Response:** The generated answer is returned to the user.

This synergistic approach ensures the chatbot can provide detailed answers grounded in its internal knowledge base while also having the flexibility to query external, up-to-date information.

## Setup

To get this project up and running, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/DevyanshiBansal/finance_chatbot](https://github.com/DevyanshiBansal/finance_chatbot)
    cd finance_chatbot
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    > **Note:** Make sure you have a `requirements.txt` file listing all your Python dependencies like `langchain`, `langchain-google-genai`, `chromadb`, `sentence-transformers`, `duckduckgo-search`, etc.

4.  **API Keys:**
    * **Google Gemini API Key:** Obtain an API key from Google AI Studio.
    * **DuckDuckGo API:** (DuckDuckGo Search is often available directly via LangChain without a separate API key, but check LangChain's documentation for any specific setup if needed).

    Set these as environment variables:
    ```bash
    export GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
    # export DUCKDUCKGO_API_KEY="YOUR_DUCKDUCKGO_API_KEY" # if required
    ```

    Or create a `.env` file in the root directory:
    ```ini
    GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
    # DUCKDUCKGO_API_KEY="YOUR_DUCKDUCKGO_API_KEY"
    ```

5.  **Prepare your Financial Data:**
    * Place your financial documents (e.g., PDFs, text files, CSVs) in a designated directory (e.g., `data/`).
    * Run the data ingestion script (you'll need to create this) to load and embed your data into ChromaDB. Example:
        ```bash
        python ingest_data.py
        ```

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

Author:
Devyanshi Bansal
