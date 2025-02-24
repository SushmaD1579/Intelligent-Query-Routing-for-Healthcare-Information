import os
from langchain.tools import TavilySearchResults
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API key from environment
api_key = os.getenv("TAVILY_API_KEY")
if not api_key:
    raise ValueError("TAVILY_API_KEY is missing. Add it to your .env file.")

# Initialize TavilySearchResults
tavily = TavilySearchResults()

# Function to perform web search
def web_search_tool(query, max_results=3):
    """
    Searches the web using Tavily API and returns search results.
    """
    try:
        results = tavily.run(
            tool_input=query,
            max_results=max_results,
            search_depth="advanced",
        )
        return results
    except Exception as e:
        return f"Error during web search: {str(e)}"

