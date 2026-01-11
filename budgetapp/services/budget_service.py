from datetime import datetime


def calculate_total_spent(transactions, category=None, start_date=None, end_date=None):
    total = 0

    for tx in transactions:
        # type = expense seulement
        if tx["type"] != "expense":
            continue

        # filtre catégorie
        if category and tx["category"] != category:
            continue

        # filtre date début
        if start_date:
            if tx["date"] < start_date:
                continue

        # filtre date fin
        if end_date:
            if tx["date"] > end_date:
                continue

        total += tx["amount"]

    return total
