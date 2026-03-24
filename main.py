from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Load file
loader = TextLoader("data.txt")
documents = loader.load()

# Split by lines
docs = []
for doc in documents:
    lines = doc.page_content.split("\n")
    for line in lines:
        if line.strip():
            docs.append(Document(page_content=line))

# Embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Store
db = Chroma.from_documents(docs, embeddings)

# Chatbot
while True:
    query = input("Ask question: ")
    if query == "exit":
        break

    results = db.similarity_search(query, k=1)
    print("Answer:", results[0].page_content)