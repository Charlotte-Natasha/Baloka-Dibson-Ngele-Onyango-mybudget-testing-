import pytest
from budgetapp.storage.db import init_db, get_connection
from budgetapp.storage.budget import (
    create_budget,
    get_budget,
    list_budgets,
    delete_budget,
    get_budget_status
)
from budgetapp.storage.transactions import create_transaction


# -------------------------------
# Setup / Teardown
# -------------------------------

@pytest.fixture(autouse=True)
def setup_db():
    # Make sure tables exist
    init_db()

    # ✅ CLEAN TABLES BEFORE EACH TEST
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM transactions")
    cur.execute("DELETE FROM budgets")
    conn.commit()
    conn.close()

    yield
# -------------------------------
# Test CRUD operations
# -------------------------------

def test_create_and_get_budget():
    create_budget("Food", "2025-01", 300)
    b = get_budget("Food", "2025-01")
    assert b is not None
    assert b["category"] == "Food"
    assert b["period"] == "2025-01"
    assert b["amount"] == 300

def test_list_budgets():
    create_budget("Food", "2025-01", 300)
    create_budget("Transport", "2025-01", 150)

    budgets = list_budgets()
    categories = [b["category"] for b in budgets]

    assert "Food" in categories
    assert "Transport" in categories


def test_delete_budget():
    delete_budget("Transport", "2025-01")
    b = get_budget("Transport", "2025-01")
    assert b is None


# -------------------------------
# Test get_budget_status (integration with transactions)
# -------------------------------

def test_get_budget_status_no_transactions():
    create_budget("Entertainment", "2025-01", 200)

    status = get_budget_status("Entertainment", "2025-01")

    assert status["total_spent"] == 0
    assert status["remaining"] == 200


def test_get_budget_status_with_transactions():
    create_budget("Entertainment", "2025-01", 200)  # ← YOU MISSED THIS

    conn = get_connection()
    create_transaction(conn, {"amount": 50, "category": "Entertainment", "date": "2025-01-05", "type": "expense"})
    create_transaction(conn, {"amount": 100, "category": "Entertainment", "date": "2025-01-10", "type": "expense"})
    conn.close()

    status = get_budget_status("Entertainment", "2025-01")

def test_get_budget_status_exceeded():
    create_budget("Entertainment", "2025-01", 200)  # ← ALSO MISSING

    conn = get_connection()
    create_transaction(conn, {"amount": 50, "category": "Entertainment", "date": "2025-01-05", "type": "expense"})
    create_transaction(conn, {"amount": 100, "category": "Entertainment", "date": "2025-01-10", "type": "expense"})
    create_transaction(conn, {"amount": 100, "category": "Entertainment", "date": "2025-01-15", "type": "expense"})
    conn.close()

    status = get_budget_status("Entertainment", "2025-01")

