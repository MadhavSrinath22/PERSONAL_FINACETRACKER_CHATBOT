# 💰 Personal Finance Tracker Chatbot

An AI-powered personal finance assistant that helps you **analyze spending patterns, answer natural-language questions about your expenses, and provide actionable financial insights** using transaction data.

This project combines **data analytics, Retrieval-Augmented Generation (RAG), and Large Language Models (LLMs)** to deliver structured, explainable financial insights.

---

## 🚀 Features

- 📊 **Transaction Analysis**
  - Load and analyze transaction data from CSV
  - Aggregate spending by category and merchant
  - Identify top spending areas

- 🤖 **AI-Powered Q&A**
  - Ask questions like:
    - *Where did I spend the most?*
    - *Which merchant did I spend the most on?*
    - *How can I reduce my expenses?*
  - Uses an LLM with **strict grounding in your data**

- 🧠 **Retrieval-Augmented Generation (RAG)**
  - Embeddings-based retrieval over transaction summaries
  - Ensures responses are based only on your spending data

- 📈 **Visual Insights**
  - Monthly spending visualization using Matplotlib

- 🔐 **Secure API Key Handling**
  - API keys managed via `.env`
  - Secrets excluded from version control

---

## 🗂️ Project Structure

.
├── app.py # Main application entry point
├── requirements.txt # Python dependencies
├── data/
│ └── transactions.csv # Transaction dataset
├── src/
│ ├── init.py
│ ├── analytics.py # Spending analytics & summaries
│ ├── categorizer.py # Transaction categorization
│ ├── merchants.py # Merchant-level analysis
│ ├── data_loader.py # CSV loading utilities
│ ├── embeddings.py # Embedding generation
│ ├── rag.py # RAG logic
│ ├── llm.py # LLM prompts & responses
│ └── config.py # Environment & API key management
└── .gitignore


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/MadhavSrinath22/PERSONAL_FINACETRACKER_CHATBOT.git
cd PERSONAL_FINACETRACKER_CHATBOT

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Create a .env File
GROQ_API_KEY=your_api_key_here

▶️ Running the Application
python app.py

You will be prompted with:

Ask about your spending (or type 'exit'):

🧠 Example Questions

Which category did I spend the most on?

Which merchant did I spend the most on?

Why was Uber categorized as transport?

How can I reduce my expenses?

Summarize my spending behavior

🧾 Example Output
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

🛠️ Technologies Used

Python

Pandas, NumPy

Matplotlib

Groq LLM (LLaMA 3)

Sentence Transformers(Hugging Face)

Retrieval-Augmented Generation (RAG)

🎯 Learning Outcomes

Designed a modular Python application

Implemented RAG for grounded AI responses

Integrated LLM APIs securely

Built an end-to-end AI-powered analytics tool

Followed production-grade project structure

📌 Future Improvements

Web UI using Streamlit

Persistent storage with a database

Budget alerts and anomaly detection

Multi-user support

👤 Author

Madhav Srinath
Graduate Student @University of Waterloo– Electrical & Computer Engineering

