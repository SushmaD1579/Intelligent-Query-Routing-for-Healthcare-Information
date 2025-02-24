# vector_db_setup.py

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma


# Load the PDF document
def load_document(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()

# Split the document into smaller chunks
def split_text(documents, chunk_size=1000, chunk_overlap=200):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return text_splitter.split_documents(documents)

# Create and store embeddings in ChromaDB
def create_vector_db(file_path, db_path="chroma_db"):
    # Load the PDF file
    documents = load_document(file_path)

    # Split into chunks
    chunks = split_text(documents)

   # Initialize HuggingFace Embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Store embeddings in ChromaDB
    vector_store = Chroma.from_documents(chunks, embeddings, persist_directory=db_path)

    print(f"✅ ChromaDB Vector Database created at: {db_path}")

# Run this script once to index the PDF
if __name__ == "__main__":
    file_path = "/Users/sushmad98/Documents/LLM Project/resources/DM_Manual.pdf"  # Change this to your actual PDF
    create_vector_db(file_path)