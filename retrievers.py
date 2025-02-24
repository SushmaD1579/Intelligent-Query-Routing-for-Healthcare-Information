# retrievers.py

# Import necessary modules
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from tavily import TavilyClient

# Vector Retriever (FAISS example)
vector_store = FAISS.load_local("path_to_faiss_index", OpenAIEmbeddings())

def vector_retriever(query):
    """
    Retrieves the top 3 most relevant documents from a vector DB (FAISS) based on the query.
    """
    results = vector_store.similarity_search(query=query, k=3)
    return [result['text'] for result in results]

# Web Search Tool (using Tavily)
tavily = TavilyClient(api_key="your_api_key")

def web_search_retriever(query):
    """
    Retrieves search results from the web for the provided query using Tavily API.
    """
    response = tavily.search(query=query)
    return response['results']
