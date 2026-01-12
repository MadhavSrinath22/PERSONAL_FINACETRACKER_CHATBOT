# Personal Finance Tracker Chatbot (RAG-based)

The **Personal Finance Tracker Chatbot** is an **interactive, Retrieval-Augmented Generation (RAG) powered finance assistant** that analyzes personal transaction data and answers natural language questions about spending patterns, categories, merchants, and trends.

The system combines **rule-based analytics**, **semantic search over transaction embeddings**, and a **large language model (LLM)** to deliver **accurate, grounded, and explainable financial insights**, avoiding hallucinations by strictly using user-provided data.

This project demonstrates an end-to-end **RAG pipeline applied to structured financial data**, built using Python and modular system design.

---

## 🚀 Key Features

* **Transaction Categorization**
  * Rule-based keyword matching across merchant and description fields
  * Transparent and explainable category assignment

* **Spending Analytics**
  * Category-wise totals and transaction counts
  * Monthly spending summaries and breakdowns
  * Merchant-level aggregation and ranking

* **Retrieval-Augmented Generation (RAG)**
  * Transactions embedded using Sentence Transformers
  * Semantic search retrieves relevant transactions per query
  * LLM responses grounded only in retrieved + computed context

* **Natural Language Q&A**
  * Ask questions like:
    * “Which category did I spend the most on?”
    * “Which merchant did I spend the most at?”
    * “Explain why Amazon was categorized as Shopping”
    * “Show my monthly transaction breakdown”

* **Explainability-first Design**
  * Explicit prompts restrict the LLM from guessing
  * Category explanations supported with transaction context

* **Modular Codebase**
  * Clean separation of data loading, analytics, embeddings, RAG logic, and LLM interaction
  * Easy to extend to UI frameworks like Streamlit

---

## 🧠 Motivation

Most finance chatbots either:
* Rely entirely on LLMs (leading to hallucinations), or
* Provide static dashboards without conversational intelligence

This project bridges the gap by:
* **Anchoring LLM reasoning to real transaction data**
* **Combining deterministic analytics with semantic retrieval**
* **Ensuring transparency and correctness in financial insights**

The result is a **trustworthy personal finance assistant** suitable for real-world extensions.

## 🏗️ System Architecture

---
+------------------------+
| User (CLI / UI) |
+-----------+------------+
|
v
+------------------------+
| Query Router (app.py) |
+-----------+------------+
|
-------------------------
| | |
v v v
Analytics RAG Engine Rule-based
(stats.py) (embeddings) Categorization
| |
-----------+
|
v
+------------------------+
| Context Builder |
+-----------+------------+
|
v
+------------------------+
| LLM (Groq / LLaMA) |
+------------------------+
|
v
+------------------------+
| Structured Answer |
+------------------------+

---

## ⚙️ Methodology Overview

### Transaction Processing
* CSV transaction data loaded via Pandas
* Dates normalized and categories assigned

### Analytics Layer
* Group-by aggregations for:
  * Category totals
  * Monthly summaries
  * Merchant-wise spending
* Deterministic computations ensure correctness

### Embedding & Retrieval
* Each transaction converted into descriptive text
* Embedded using `all-MiniLM-L6-v2`
* Cosine similarity used for semantic search

### RAG Prompting
* Retrieved transactions injected into prompt
* LLM instructed to:
  * Use only provided context
  * Follow a strict response structure
  * Avoid assumptions

---

## 📂 Project Structure

PERSONAL_FINACETRACKER_CHATBOT/
├── app.py # Main application entry point
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
├── data/
│ └── transactions.csv # Sample transaction dataset
├── src/
│ ├── init.py
│ ├── config.py # Environment & API key loading
│ ├── data_loader.py # CSV loading utilities
│ ├── categorizer.py # Transaction categorization logic
│ ├── analytics.py # Spending analytics & summaries
│ ├── merchants.py # Merchant-level utilities
│ ├── embeddings.py # Embedding generation
│ ├── rag.py # Semantic retrieval logic
│ └── llm.py # LLM prompting & response handling


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/MadhavSrinath22/PERSONAL_FINACETRACKER_CHATBOT.git
cd PERSONAL_FINACETRACKER_CHATBOT

### 1️⃣ Clone the Repository
2️⃣ Install Dependencies
pip install -r requirements.txt

###3️⃣ Configure API Key
Create a .env file in the project root:
GROQ_API_KEY=your_api_key_here

###4️⃣ Run the Application

---
##💬 Example Questions You Can Ask

“Which category did I spend the most on?”

“Which merchant did I spend the most at?”

“Show my monthly transaction breakdown”

“Why was Starbucks categorized as Coffee?”

“What were my top merchants last month?”

“Explain my spending pattern”
---

## Author

Madhav Srinath

Graduate Student @ University of Waterloo– Electrical & Computer Engineering
Focus Areas: Embedded Systems, Distributed Systems, Machine Learning, RAG Architectures
---
📄 License
This project is released for educational and personal use.
