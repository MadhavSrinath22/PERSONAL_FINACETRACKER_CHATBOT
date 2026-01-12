# SpendWise AI- Personal Finance Tracker Chatbot (RAG-based)

 **SpendWise AI**,a **Personal Finance Tracker Chatbot** is an **interactive, Retrieval-Augmented Generation (RAG) powered finance assistant** that analyzes personal transaction data and answers natural language questions about spending patterns, categories, merchants, and trends.

The system combines **rule-based analytics**, **semantic search over transaction embeddings**, and a **large language model (LLM)** to deliver **accurate, grounded, and explainable financial insights**, avoiding hallucinations by strictly using user-provided data.

This project demonstrates an end-to-end **RAG pipeline applied to structured financial data**, built using Python and modular system design.

---

## 🚀 Key Features

- **Transaction Categorization**
  - Rule-based keyword matching across merchant and description fields
  - Transparent and explainable category assignment

- **Spending Analytics**
  - Category-wise totals and transaction counts
  - Monthly spending summaries and breakdowns
  - Merchant-level aggregation and ranking

- **Retrieval-Augmented Generation (RAG)**
  - Transactions embedded using Sentence Transformers
  - Semantic search retrieves relevant transactions per query
  - LLM responses grounded only in retrieved + computed context

- **Natural Language Q&A**
  - Ask questions like:
    - “Which category did I spend the most on?”
    - “Which merchant did I spend the most at?”
    - “Explain why Amazon was categorized as Shopping”
    - “Show my monthly transaction breakdown”

- **Explainability-first Design**
  - Explicit prompts restrict the LLM from guessing
  - Category explanations supported with transaction context

- **Modular Codebase**
  - Clean separation of data loading, analytics, embeddings, RAG logic, and LLM interaction
  - Easy to extend to UI frameworks like Streamlit

---

## 🧠 Motivation

Most finance chatbots either:
- Rely entirely on LLMs (leading to hallucinations), or
- Provide static dashboards without conversational intelligence

This project bridges the gap by:
- **Anchoring LLM reasoning to real transaction data**
- **Combining deterministic analytics with semantic retrieval**
- **Ensuring transparency and correctness in financial insights**

---

## 🏗️ System Architecture

```text
+------------------------+
|   User (CLI / UI)      |
+-----------+------------+
            |
            v
+------------------------+
|  Query Router (app.py) |
+-----------+------------+
            |
     -------------------------
     |          |            |
     v          v            v
Analytics   RAG Engine   Rule-based
(analytics) (embeddings) Categorization
     |          |
     -----------+
            |
            v
+------------------------+
|   Context Builder      |
+-----------+------------+
            |
            v
+------------------------+
|   LLM (Groq / LLaMA)   |
+------------------------+
            |
            v
+------------------------+
| Structured Answer     |
+------------------------+
```
---
📂 Project Structure
---
```text
PERSONAL_FINACETRACKER_CHATBOT/
├── app.py
├── requirements.txt
├── .gitignore
├── data/
│   └── transactions.csv
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_loader.py
│   ├── categorizer.py
│   ├── analytics.py
│   ├── merchants.py
│   ├── embeddings.py
│   ├── rag.py
│   └── llm.py
```
---
⚙️ Setup Instructions
---
1️⃣ Clone the Repository
```bash
git clone https://github.com/MadhavSrinath22/PERSONAL_FINACETRACKER_CHATBOT.git
cd PERSONAL_FINACETRACKER_CHATBOT
```
2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
3️⃣ Configure API Key
Create a .env file in the project root:
```bash
GROQ_API_KEY=your_api_key_here
```
4️⃣ Run the Application
```bash
python app.py
```
---
💬 Example Questions You Can Ask
---
Which category did I spend the most on?

Which merchant did I spend the most at?

Show my monthly transaction breakdown

Why was Starbucks categorized as Coffee?

What were my top merchants last month?

Explain my spending pattern

---

🧾 Example Output
---
```bash
AI Insight:

Main insight:
- You spent the most on Groceries.

Details:
1. Total spent on Groceries: $200.50
2. Frequent grocery transactions detected
3. Groceries account for the largest share of expenses

Suggestions:
1. Set a monthly grocery budget
2. Compare prices across stores
3. Track impulse purchases
```
---
👤 Author
---
Madhav Srinath Thanigaivel 

Graduate Student – MEng Electrical & Computer Engineering
University of Waterloo

---
📄 License
---
This project is released for educational and personal use.


