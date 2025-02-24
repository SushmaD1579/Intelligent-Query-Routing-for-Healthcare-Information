from langgraph.graph import StateGraph
from router import route_query
from retrievers import vector_retriever, web_search_retriever
from llm_config import llm_answer

# Create the workflow graph
workflow = StateGraph()

# Define nodes
workflow.add_node("route_query", route_query)
workflow.add_node("vector_retriever", vector_retriever)
workflow.add_node("web_search", web_search_retriever)
workflow.add_node("answer_generation", llm_answer)

# Define conditional routing
workflow.add_conditional_edges(
    "route_query",
    {
        "vector_only": "vector_retriever",
        "web_only": "web_search",
        "both": ["vector_retriever", "web_search"]
    }
)

# Connect retrievers to answer generation
workflow.add_edge("vector_retriever", "answer_generation")
workflow.add_edge("web_search", "answer_generation")

# Set entry and exit points
workflow.set_entry_point("route_query")
workflow.set_exit_point("answer_generation")

# Compile the graph
graph = workflow.compile()

workflow.visualize()  # This will generate a visual graph of your workflow
