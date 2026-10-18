import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

docs_dir = "docs"
all_documents = []

print("Scanning directory for PDFs...")
for filename in os.listdir(docs_dir):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(docs_dir, filename)
        print(f"Reading: {pdf_path}...")
        loader = PyMuPDFLoader(pdf_path)
        all_documents.extend(loader.load())

print(f"\nSuccessfully read a total of {len(all_documents)} pages.")

# Text chunking
print("Splitting text into smaller, readable chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = text_splitter.split_documents(all_documents)
print(f"Split into {len(chunks)} total chunks.")

# Embedding model
print("Loading embedding model (BAAI/bge-m3)...")
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")

# Build FAISS vector database
print("Building vector database (This might take a few minutes for large PDFs)...")
db = FAISS.from_documents(chunks, embeddings)

# Save database locally
db_dir = "faiss_index"
db.save_local(db_dir)

print(f"Done! The complete BMW knowledgebase is built and saved to: {db_dir}")