# test de la fonction Calcul des dépenses totales: 

from budgetapp.services.budget_service import calculate_total_spent


def test_calculate_total_spent_for_category_and_period():
    transactions = [
        {"amount": 50, "category": "Food", "date": "2025-01-10", "type": "expense"},
        {"amount": 20, "category": "Food", "date": "2025-01-15", "type": "expense"},
        {"amount": 30, "category": "Transport", "date": "2025-01-10", "type": "expense"},
        {"amount": 100, "category": "Food", "date": "2025-02-01", "type": "expense"},
    ]

    total = calculate_total_spent(
        transactions,
        category="Food",
        start_date="2025-01-01",
        end_date="2025-01-31",
    )

    assert total == 70




# test de la fonction calculate_remaining_budget : 

from budgetapp.services.budget_service import calculate_remaining_budget


def test_calculate_remaining_budget_under_limit():
    total_spent = 70
    budget_amount = 200

    remaining = calculate_remaining_budget(total_spent, budget_amount)

    assert remaining == 130


def test_calculate_remaining_budget_over_limit():
    total_spent = 250
    budget_amount = 200

    remaining = calculate_remaining_budget(total_spent, budget_amount)

    assert remaining == -50
