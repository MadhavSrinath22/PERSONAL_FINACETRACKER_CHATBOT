import sys
sys.path.append("/content/src")


from groq import Groq

from src.config import GROQ_API_KEY
from data_loader import load_transactions
from categorizer import add_category_column
from analytics import (
    compute_stats,
    monthly_transactions_summary,
    monthly_summary,
    build_full_context
)
from merchants import (
    get_transaction_by_merchant,
    compute_merchant_stats,
    format_merchant_summary
)
from embeddings import build_transaction_embeddings
from rag import build_rag_context
from llm import ask_ai_about_spending, explain_transaction_category



def plot_monthly_spending(monthly_df):
    import matplotlib.pyplot as plt
    monthly_df.plot(kind="bar", stacked=True, figsize=(12, 6))
    plt.title("Monthly Spending by Category")
    plt.ylabel("Amount ($)")
    plt.xlabel("Month")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    plt.show(block=False)
    plt.pause(0.1)


df = load_transactions()
df = add_category_column(df)

total_spent, by_category, txns_per_category, avg_txn = compute_stats(df)
txn_texts, txn_embeddings = build_transaction_embeddings(df)

monthly_df = monthly_summary(df)
plot_monthly_spending(monthly_df)


monthly_txn_summary = monthly_transactions_summary(df)

merchant_spend, merchant_txn_count, top_merchants = compute_merchant_stats(df)
merchant_summary = format_merchant_summary(
    merchant_spend,
    merchant_txn_count,
    top_merchants
)

full_context = build_full_context(
    by_category,
    txns_per_category,
    total_spent,
    avg_txn,
    monthly_txn_summary,
    merchant_summary
)


client = Groq(api_key=GROQ_API_KEY)



merchant_spend = df.groupby("Merchant")["Amount"].sum()

while True:
    user_query = input("\nAsk about your spending (or type 'exit'): ").strip()

    if user_query.lower() in ("exit", "quit"):
        break

    query_lower = user_query.lower()

 
    if any(phrase in query_lower for phrase in [
        "spend the most",
        "most spent",
        "highest spending",
        "top category"
    ]):
        top_category = by_category.idxmax()
        amount = by_category.max()

        structured_context = (
            f"Top spending category:\n"
            f"- {top_category}: ${amount:.2f}\n"
        )

        ask_ai_about_spending(
            client,
            structured_context,
            user_query
        )
        continue


    if any(word in query_lower for word in ["why", "explain"]):
        found = False

        for merchant in df["Merchant"].unique():
            if merchant.lower() in query_lower:
                row = get_transaction_by_merchant(df, merchant)
                if row is not None:
                    explanation = explain_transaction_category(client, row)
                    print("\nAI Insight:")
                    print(explanation)
                    found = True
                break

        if not found:
            print("\nAI Insight:")
            print("Please mention a specific merchant to explain a transaction.")
        continue
    rag_context = build_rag_context(user_query, txn_texts, txn_embeddings)
    combined_context = f"{full_context}\n\n{rag_context}"

    ask_ai_about_spending(
        client,
        combined_context,
        user_query
    )

