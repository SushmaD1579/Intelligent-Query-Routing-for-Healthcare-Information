from prompts import manual_static_data_prompt, web_search_data_prompt
from llm_config import llm_router

def route_query(query, use_manual_data=False):
    """
    Routes the query based on whether it should use static/manual data or real-time web search.
    """
    if use_manual_data:
        prompt = manual_static_data_prompt.format(query=query)
    else:
        prompt = web_search_data_prompt.format(query=query)

    routing_decision = llm_router.predict(prompt)

    if "Static data" in routing_decision and "Web Search" in routing_decision:
        return "both"  # Perform both calls in parallel
    elif "Static data" in routing_decision:
        return "static_data"
    else:
        return "web_search"
