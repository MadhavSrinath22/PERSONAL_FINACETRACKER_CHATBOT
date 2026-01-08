from groq import Groq

def explain_transaction_category(client, row):
    prompt = (
        f"Merchant: {row['Merchant']}\n"
        f"Description: {row.get('Description','')}\n"
        f"Amount: ${row['Amount']:.2f}\n"
        f"Assigned category: {row['Category']}\n\n"
        "Explain why this category makes sense."
    )

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a finance expert."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
        max_completion_tokens=200,
    )

    return completion.choices[0].message.content


def ask_ai_about_spending(client, context, user_query):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful personal finance assistant. "
                "You analyze the user's spending data and give clear, practical advice. "
                "Use ONLY the data provided in the spending summary. "
                "If something is not in the data, say that you don't know instead of guessing."
            ),
        },
        {
            "role": "user",
            "content": (
                f"My spending data:\n{context}\n\n"
                f"User question: {user_query}\n\n"
                "Please answer in this exact format:\n"
                "Main insight:\n"
                "- <one short sentence summarizing the key point>\n\n"
                "Details:\n"
                "1. <detail 1>\n"
                "2. <detail 2>\n"
                "3. <detail 3 (if relevant)>\n\n"
                "Suggestions:\n"
                "1. <specific, practical suggestion 1>\n"
                "2. <specific, practical suggestion 2>\n"
                "3. <optional extra suggestion if useful>\n"
            ),
        },
    ]

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.4,          # slightly lower for more consistent answers
        max_completion_tokens=512,
        top_p=1,
        stream=True,
    )

    print("\nAI Insight:")
    for chunk in completion:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="")
    print()  # newline at the end
