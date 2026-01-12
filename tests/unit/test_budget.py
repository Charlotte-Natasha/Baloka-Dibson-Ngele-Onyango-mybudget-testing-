# tests de la fonction << Calcul des dépenses totales >> : 

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




# tests de la fonction << calculate_remaining_budget >> : 

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





# tests de la fonction << calculate_consumption_percentage >> : 

from budgetapp.services.budget_service import calculate_consumption_percentage


def test_calculate_consumption_percentage_normal():
    total_spent = 50
    budget_amount = 200

    percent = calculate_consumption_percentage(total_spent, budget_amount)

    assert percent == 25


def test_calculate_consumption_percentage_over_budget():
    total_spent = 300
    budget_amount = 200

    percent = calculate_consumption_percentage(total_spent, budget_amount)

    assert percent == 150




# tests de la fonction << is_budget_exceeded >> : 

from budgetapp.services.budget_service import is_budget_exceeded


def test_is_budget_exceeded_true():
    total_spent = 250
    budget_amount = 200

    result = is_budget_exceeded(total_spent, budget_amount)

    assert result is True


def test_is_budget_exceeded_false():
    total_spent = 150
    budget_amount = 200

    result = is_budget_exceeded(total_spent, budget_amount)

    assert result is False





# tests de la fonction << get_budget_alert >> : 

from budgetapp.services.budget_service import get_budget_alert


def test_get_budget_alert_when_exceeded():
    total_spent = 310
    budget_amount = 300

    alert = get_budget_alert(total_spent, budget_amount)

    assert alert is not None
    assert "10" in alert
    assert "103" in alert











