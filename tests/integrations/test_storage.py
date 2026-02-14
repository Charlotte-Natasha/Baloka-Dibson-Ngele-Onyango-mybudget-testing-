import pytest
from budgetapp.storage.transactions import create_transaction
from budgetapp.storage.budget import create_budget, get_budget, get_budget_status, delete_budget, list_budgets

def test_create_and_get_budget():
    create_budget("Food", "2025-01", 300)
    
    # DEBUG: Let's see if the list_budgets function sees it
    all_budgets = list_budgets()
    print(f"Current budgets in DB: {all_budgets}")
    
    budget = get_budget("Food", "2025-01")
    assert budget is not None

def test_budget_status_with_transactions():
    # Ensure tables are clean
    create_budget("Food", "2025-01", 300)
    
    # Use the helper without passing 'None' if you want to be safe
    from budgetapp.storage.db import get_connection
    conn = get_connection()
    create_transaction(conn, {"amount": 100, "category": "Food", "type": "expense", "date": "2025-01-10"})
    conn.close() # Close it so get_budget_status can open its own
    
    status = get_budget_status("Food", "2025-01")
    assert status is not None
    assert status["total_spent"] == 100

def test_delete_budget_clears_status():
    delete_budget("Food", "2025-01")
    status = get_budget_status("Food", "2025-01")
    assert status is None

