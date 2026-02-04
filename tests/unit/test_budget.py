import pytest
from budgetapp.storage.db import init_db, set_db_path
from budgetapp.storage.budget import create_budget, get_budget_status

@pytest.fixture(autouse=True)
def setup_db(tmp_path):
    """
    Isolated DB for unit tests.
    """
    db_file = tmp_path / "test_budget.db"
    set_db_path(str(db_file))
    init_db()
    yield

def test_get_budget_status_no_transactions():
    create_budget("Entertainment", "2025-01", 200)
    status = get_budget_status("Entertainment", "2025-01")
    assert status is not None
    assert status["total_spent"] == 0
    assert status["remaining"] == 200
    assert status["consumption_pct"] == 0
    assert status["exceeded"] is False
    assert status["alert"] is None

def test_budget_status_with_transactions():
    create_budget("Food", "2025-01", 300)

    from budgetapp.storage.transactions import create_transaction
    create_transaction(None, {"amount": 100, "category": "Food", "type": "expense", "date": "2025-01-10"})
    create_transaction(None, {"amount": 50, "category": "Food", "type": "expense", "date": "2025-01-15"})

    status = get_budget_status("Food", "2025-01")
    assert status is not None
    assert status["total_spent"] == 150
    assert status["remaining"] == 150
    assert status["consumption_pct"] == 50
    assert status["exceeded"] is False
    assert status["alert"] is None

def test_budget_exceeded():
    create_budget("Transport", "2025-01", 100)

    from budgetapp.storage.transactions import create_transaction
    create_transaction(None, {"amount": 120, "category": "Transport", "type": "expense", "date": "2025-01-05"})

    status = get_budget_status("Transport", "2025-01")
    assert status is not None
    assert status["total_spent"] == 120
    assert status["remaining"] == -20
    assert status["consumption_pct"] == 120
    assert status["exceeded"] is True
    # ✅ Correct assertion
    assert "Budget exceeded" in status["alert"]

