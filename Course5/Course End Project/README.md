# Course End Project - main.ipynb

## Overview
This notebook demonstrates a hybrid retrieval and routing workflow using CrewAI and LangChain tools. It builds an agent-based system that classifies user queries and routes them to either a Monday.com API knowledge retrieval tool or a general web search tool.

## Key Features
- Installs required Python packages for CrewAI, LangChain, Tavily, and FAISS.
- Loads environment variables using `dotenv`.
- Defines a custom web search tool using the Tavily search API.
- Loads a FAISS vector store and creates a retrieval-based QA chain for Monday.com API documentation.
- Builds a request routing agent that classifies input as either `MONDAY` or `OTHER`.
- Uses conditional agent execution to dispatch the query to the appropriate retriever.

## Notebook Sections
1. Setup environment variables
2. Import libraries and load `.env`
3. Create the Tavily web search tool
4. Create the FAISS-based Monday.com API search tool
5. Create agents for routing and retrieval
6. Define tasks for routing and retrieval
7. Execute the request and print the result

## Requirements
- Python environment with the packages listed in the notebook
- Valid `OPENAI_API_KEY` and `TAVILY_API_KEY` set in the environment or `.env`
- A local FAISS index directory at `faiss_index`

## Usage
1. Open `main.ipynb` in Jupyter or VS Code.
2. Ensure `.env` contains the required API keys.
3. Run the notebook cells sequentially.
4. Enter a query when prompted, then review the routed agent response.

## Notes
- The notebook assumes the FAISS index has already been created and stored under `faiss_index`.
- The `MondayAPIDocumentationSearchTool` is configured to query the local FAISS retriever and return answers from Monday.com documentation.
- The router returns only `MONDAY` or `OTHER` to decide which retrieval pipeline to use.
