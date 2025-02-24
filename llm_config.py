import os
from dotenv import load_dotenv
from langchain.chat_models import ChatGroq

# Load API keys from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM instances
llm_router = ChatGroq(model="mixtral-8x7b-32768", api_key=GROQ_API_KEY)
llm_answer = ChatGroq(model="mixtral-8x7b-32768", api_key=GROQ_API_KEY)
