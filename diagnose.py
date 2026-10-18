import ollama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

print("🔧 Initializing system...")
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")

print("📚 Loading BMW knowledgebase...")
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

print("-" * 50)
print("✅ Diagnostic Assistant is ready!")
print("-" * 50)

while True:
    query = input("\nEnter the fault code or symptom (or 'q' to quit): ")
    
    if query.lower() == 'q':
        print("Exiting...")
        break

    print("\n🔍 Searching the 1154-page service manual...")
    # Retrieve the 3 most relevant chunks
    matches = db.similarity_search(query, k=3)

    context = ""
    for i, match in enumerate(matches):
        context += f"\n--- Excerpt {i+1} ---\n{match.page_content}\n"

    print("🧠 Thinking based on factory data...")

    # Prompt compilation for RAG
    system_prompt = f"""
    You are a professional BMW E36 diagnostic engineer.
    Answer the user's question STRICTLY based on the provided service manual excerpts.
    If the exact value is not in the text, say "I cannot find this in the manual."
    Never mix up Voltage (V/VDC) and Resistance (Ohms/Ω). 
    List the exact connector pins, voltages, and resistances clearly.
    REPLY IN ENGLISH!

    MANUAL EXCERPTS:
    {context}
    """

    # Send request to local AI
    response = ollama.chat(model='qwen2.5:7b', messages=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': query}
    ])

    print("\n" + "="*50)
    print(" 🛠️ DIAGNOSIS & REPAIR PLAN")
    print("="*50)
    print(response['message']['content'])
    print("="*50)