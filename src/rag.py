from embeddings import semantic_search

def build_rag_context(user_query, texts, embeddings):
    relevant_txns = semantic_search(user_query, texts, embeddings)

    lines = ["Relevant transactions:"]
    for txn in relevant_txns:
        lines.append(f"- {txn}")

    return "\n".join(lines)
