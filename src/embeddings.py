import numpy as np
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def transaction_to_text(row):
    return (
        f"Transaction on {row['Date'].date()} at {row['Merchant']}. "
        f"Category: {row['Category']}. "
        f"Amount: ${row['Amount']:.2f}. "
        f"Description: {row.get('Description', '')}"
    )

def build_transaction_embeddings(df):
    texts = df.apply(transaction_to_text, axis=1).tolist()
    embeddings = embedding_model.encode(texts)
    return texts, embeddings


def semantic_search(query, texts, embeddings, top_k=5):
    query_embedding = embedding_model.encode([query])[0]
    similarities = np.dot(embeddings, query_embedding) / (
        np.linalg.norm(embeddings, axis=1)
        * np.linalg.norm(query_embedding)
    )

    top_indices = similarities.argsort()[-top_k:][::-1]
    return [texts[i] for i in top_indices]

