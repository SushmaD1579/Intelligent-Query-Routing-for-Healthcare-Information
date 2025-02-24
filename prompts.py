from langchain.prompts import PromptTemplate

# Define the prompt template for routing the query
router_prompt = PromptTemplate(
    input_variables=["query", "vector_db_metadata", "web_search_summary"],
    template="""
    You are a helpful assistant tasked with determining the best route for processing a user's query.
    
    Here is some context to help you make your decision:

    - **VectorDB Metadata Summary**: {vector_db_metadata}
    - **Web Search Summary**: {web_search_summary}

    The user's query is: "{query}"

    Based on the provided metadata and the user's query, please decide the following:
    1. Should the query be routed to VectorDB (old/static data)?
    2. Should the query be routed to Web Search (new/updated data)?
    3. Should both VectorDB and Web Search be used?

    Return one of the following options:
    - "vector_only"
    - "web_only"
    - "both"
    """
)


answer_template = """
You are a helpful assistant answering a query based on relevant information. 
Here is what you have retrieved:

- From VectorDB: {vector_db_data}
- From Web Search: {web_search_data}

User Query: "{user_query}"

Now, generate a comprehensive and relevant answer based on the retrieved data.
"""


# Prompt for answering the final answer (from both sources or just one)
final_answer_prompt = PromptTemplate(
    input_variables=["query", "context"],
    template="""
    Based on the query '{query}' and the following context:
    {context}

    Please provide a concise and informative answer.
    """
)

# You can also add other templates like a summary prompt, etc.
