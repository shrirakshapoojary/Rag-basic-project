# Rag-basic-project


This project demonstrates a simple Retrieval-Augmented Generation (RAG) pipeline using LangChain and ChromaDB.

## Features
- Loads text data
- Converts into embeddings
- Stores in vector database
- Retrieves relevant answers based on query

## Tech Stack
- Python
- LangChain
- ChromaDB
- HuggingFace Embeddings

## How to Run
```bash
pip install langchain langchain-community chromadb sentence-transformers
python main.py

## 📌 Project Explanation

### What is RAG?
**RAG (Retrieval-Augmented Generation)** is a technique used to retrieve relevant information from a given document based on semantic similarity, instead of relying only on general knowledge.

In this project, I built a simple **document-based question answering system** that answers user questions based on the content of a provided text file.

---

## 🔁 Project Flow

### 1. Load the File
The system first loads the input file using a document loader.

- The file is read and converted into a **document format**.

### 2. Split the Content
The loaded content is then split into smaller chunks.

- In this project, the text is split **line by line**.
- Each line is treated as a separate **document chunk**.

### 3. Convert Text into Embeddings
Each document chunk is converted into **embeddings** using a **Hugging Face embedding model**.

- **Embeddings** are numerical vector representations of text.
- They help the system understand the **semantic meaning** of the content.

### 4. Store in Vector Database
The generated embeddings are stored in a **vector database**.

- In this project, **Chroma DB** is used.
- It stores the document chunks along with their vector representations.

### 5. Ask Questions
When a user asks a question:

- The query is also converted into an **embedding**.
- The system performs **similarity search** in the vector database.

### 6. Retrieve the Answer
The vector database finds the **most semantically similar document chunk** to the user’s query.

- That most relevant result is returned as the **answer**.

---

## 🧠 In Short

**Flow:**  
`Load File → Split into Chunks → Convert to Embeddings → Store in Chroma DB → Ask Query → Similarity Search → Return Answer`

---

## 🚀 Purpose of the Project
This project helps users quickly find answers from a specific document without manually searching through the entire file.

It can be useful for:
- Notes-based Q&A
- Syllabus assistants
- PDF/document chatbots
- College material search systems