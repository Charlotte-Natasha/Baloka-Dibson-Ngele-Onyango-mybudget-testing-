from datetime import datetime


# 1 ere fonction : << Calcul des dépenses totales >>

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




# 2 eme fonction : << calculate_remaining_budget >>

def calculate_remaining_budget(total_spent, budget_amount):
    """
    Retourne le budget restant.
    Peut être négatif si le budget est dépassé.
    """
    return budget_amount - total_spent





# 3 eme fonction : << calculate_consumption_percentage >>


def calculate_consumption_percentage(total_spent, budget_amount):
    """
    Retourne le pourcentage du budget consommé.
    Peut dépasser 100 si le budget est dépassé.
    """
    if budget_amount == 0:
        raise ValueError("Le budget ne peut pas être égal à 0.")

    return int((total_spent / budget_amount) * 100)




# 4 eme fonction : << is_budget_exceeded >>

def is_budget_exceeded(total_spent, budget_amount):
    """
    Retourne True si le budget est dépassé, sinon False.
    """
    return total_spent > budget_amount





# 5 eme fonction : << get_budget_alert >>


def get_budget_alert(total_spent, budget_amount):
    if budget_amount == 0:
        return None

    if total_spent <= budget_amount:
        return None

    over = total_spent - budget_amount
    percentage = (total_spent / budget_amount) * 100

    return f"Budget exceeded by {over} ({percentage:.1f}%)"












