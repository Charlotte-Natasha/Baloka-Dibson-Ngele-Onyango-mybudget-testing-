import pytest
from budgetapp.services.budget_service import (
    calculate_total_spent,
    calculate_remaining_budget,
    calculate_consumption_percentage,
    is_budget_exceeded,
    get_budget_alert
)

# -------------------------------
# Test calculate_total_spent
# -------------------------------

def test_calculate_total_spent_basic():
    transactions = [
        {"amount": 50, "category": "Food", "date": "2025-01-10", "type": "expense"},
        {"amount": 30, "category": "Food", "date": "2025-01-15", "type": "expense"},
        {"amount": 20, "category": "Transport", "date": "2025-01-12", "type": "expense"},
        {"amount": 100, "category": "Food", "date": "2025-02-01", "type": "expense"},
        {"amount": 200, "category": "Income", "date": "2025-01-05", "type": "income"},
    ]
    total_food = calculate_total_spent(transactions, category="Food")
    total_transport = calculate_total_spent(transactions, category="Transport")
    total_income = calculate_total_spent(transactions, category="Income")
    
    assert total_food == 180  # 50 + 30 + 100
    assert total_transport == 20
    assert total_income == 0  # type != expense ignored

# -------------------------------
# Test calculate_remaining_budget
# -------------------------------

def test_calculate_remaining_budget_under_and_over():
    assert calculate_remaining_budget(80, 100) == 20
    assert calculate_remaining_budget(120, 100) == -20

# -------------------------------
# Test calculate_consumption_percentage
# -------------------------------

def test_calculate_consumption_percentage_normal_and_over():
    assert calculate_consumption_percentage(50, 200) == 25
    assert calculate_consumption_percentage(300, 200) == 150

def test_calculate_consumption_percentage_zero_budget():
    with pytest.raises(ValueError):
        calculate_consumption_percentage(50, 0)

# Test is_budget_exceeded

def test_is_budget_exceeded_true_false():
    assert is_budget_exceeded(150, 100) is True
    assert is_budget_exceeded(50, 100) is False

# Test get_budget_alert

def test_get_budget_alert_none_and_exceeded():
    alert_none = get_budget_alert(50, 100)
    alert_exceeded = get_budget_alert(120, 100)
    
    assert alert_none is None
    assert alert_exceeded is not None
    assert "20" in alert_exceeded  # amount exceeded
    assert "120" in alert_exceeded  # percent spent

def test_get_budget_alert_zero_budget():
    assert get_budget_alert(50, 0) is None
