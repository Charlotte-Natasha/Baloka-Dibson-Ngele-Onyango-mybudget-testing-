from datetime import datetime
from budgetapp.config import BUDGET_WARNING_THRESHOLD

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

    consumption_pct = (total_spent / budget_amount) * 100

    # ⚠️ Warning if 80% ≤ consumption < 100%
    if BUDGET_WARNING_THRESHOLD <= consumption_pct < 100:
        return f"Warning: Budget at {consumption_pct:.1f}% consumed"

    # ❌ Exceeded budget
    if total_spent > budget_amount:
        over = total_spent - budget_amount
        return f"Budget exceeded by {over} ({consumption_pct:.1f}%)"

    # ✅ No alert
    return None

