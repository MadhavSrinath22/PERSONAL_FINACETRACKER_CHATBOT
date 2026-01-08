def compute_stats(df):
    total_spent = df['Amount'].sum()
    by_category = df.groupby("Category")['Amount'].sum().sort_values(ascending=False)
    txns_per_category = df['Category'].value_counts()
    avg_txn = df['Amount'].mean()
    return total_spent, by_category, txns_per_category, avg_txn
    
def monthly_summary(df):
    return (
        df.groupby([df["Date"].dt.to_period("M"), "Category"])["Amount"]
        .sum()
        .unstack(fill_value=0)
    )

def monthly_transactions_summary(df):
    lines = []
    grouped = df.groupby(df['Date'].dt.to_period('M'))
    for period, group in grouped:
        lines.append(f"{period} ({len(group)} transactions):")
        for _, row in group.iterrows():
            lines.append(
                f"- {row['Date'].date()} | {row['Merchant']} | "
                f"{row['Category']} | ${row['Amount']:.2f}"
            )
        lines.append("")
    return "\n".join(lines)

def build_full_context(
    by_category,
    txns_per_category,
    total_spent,
    avg_txn,
    monthly_txn_summary,
    merchant_summary
):
    summary_lines = [f"{cat}: ${amt:.2f}" for cat, amt in by_category.items()]
    summary_text = "\n".join(summary_lines)

    txn_lines = [
        f"{cat}: {count} transactions"
        for cat, count in txns_per_category.items()
    ]
    txn_text = "\n".join(txn_lines)

    stats_text = (
        f"Total spent: ${total_spent:.2f}\n"
        f"Average transaction: ${avg_txn:.2f}"
    )

    full_context = (
        "Spending by category (overall):\n"
        f"{summary_text}\n\n"
        "Transaction count by category:\n"
        f"{txn_text}\n\n"
        "Monthly transaction breakdown:\n"
        f"{monthly_txn_summary}\n\n"
        "Overall stats:\n"
        f"{stats_text}\n\n"
        "Merchant-level spending:\n"
        f"{merchant_summary}"
    )

    return full_context


