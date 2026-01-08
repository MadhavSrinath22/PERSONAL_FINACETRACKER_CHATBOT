def compute_merchant_stats(df, top_n=5):
    merchant_spend = (
        df.groupby("Merchant")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    merchant_txn_count = (
        df.groupby("Merchant")["Amount"]
        .count()
        .sort_values(ascending=False)
    )

    top_merchants = merchant_spend.head(top_n)
    return merchant_spend, merchant_txn_count, top_merchants


def format_merchant_summary(merchant_spend, merchant_txn_count, top_merchants):
    lines = ["Top merchants by total spending:"]
    for merchant, amt in top_merchants.items():
        count = merchant_txn_count.get(merchant, 0)
        lines.append(
            f"- {merchant}: ${amt:.2f} across {count} transactions"
        )
    return "\n".join(lines)


def get_transaction_by_merchant(df, merchant_name):
    matches = df[
        df["Merchant"].str.lower().str.contains(merchant_name.lower())
    ]
    if matches.empty:
        return None
    return matches.iloc[0]

