categories = {
    "Food": ["restaurant", "dining", "mcdonalds", "burger", "pizza"],
    "Coffee": ["starbucks", "coffee", "cafe"],
    "Groceries": ["supermarket", "grocery", "walmart", "target", "whole foods"],
    "Transport": ["uber", "lyft", "metro", "bus", "taxi", "fuel", "gas"],
    "Entertainment": ["netflix", "spotify", "movie", "cinema", "amc"],
    "Shopping": ["amazon", "mall", "clothes", "nike", "adidas"],
    "Bills": ["electric", "water", "internet", "phone", "rent"]
}

def categorize(row):
    text = f"{row['Merchant']} {row.get('Description','')}".lower()
    for cat, keywords in categories.items():
        if any(k in text for k in keywords):
            return cat
    return "Other"

def add_category_column(df):
    df["Category"] = df.apply(categorize, axis=1)
    return df
