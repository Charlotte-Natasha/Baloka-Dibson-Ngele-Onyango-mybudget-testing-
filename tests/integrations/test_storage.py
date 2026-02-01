import pytest
from budgetapp.storage.transactions import create_transaction
from budgetapp.storage.budget import create_budget, get_budget, get_budget_status, delete_budget

def test_create_and_get_budget():
    create_budget("Food", "2025-01", 300)
    budget = get_budget("Food", "2025-01")
    assert budget is not None
    assert budget["category"] == "Food"
    assert budget["period"] == "2025-01"
    assert budget["amount"] == 300

def test_budget_status_with_transactions():
    # Add transactions
    create_transaction(None, {"amount": 100, "category": "Food", "type": "expense", "date": "2025-01-10"})
    create_transaction(None, {"amount": 50, "category": "Food", "type": "expense", "date": "2025-01-15"})
    
    status = get_budget_status("Food", "2025-01")
    
    assert status["total_spent"] == 150
    assert status["remaining"] == 150
    assert status["consumption_pct"] == 50
    assert status["exceeded"] is False
    assert status["alert"] is None

def test_delete_budget_clears_status():
    delete_budget("Food", "2025-01")
    status = get_budget_status("Food", "2025-01")
    assert status is None
