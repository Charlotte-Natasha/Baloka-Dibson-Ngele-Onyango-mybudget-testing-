import pytest
from click.testing import CliRunner
from budgetapp.cli.app import cli
from budgetapp.storage.db import init_db, set_db_path

from budgetapp.storage.budget import create_budget

@pytest.fixture(autouse=True)
def setup_db(tmp_path):
    """
    Create an isolated DB for each test using tmp_path.
    """
    db_file = tmp_path / "test_budget.db"
    set_db_path(str(db_file))  # point DB_PATH to temp file
    init_db()  # create tables
    yield
    # no cleanup needed, tmp_path is auto-cleaned

def test_add_transaction_and_check_budget():
    runner = CliRunner()

    # 1️⃣ Add a budget
    result = runner.invoke(cli, ["add-budget", "Food", "2025-01", "300"])
    assert result.exit_code == 0
    assert "Budget created" in result.output

    # 2️⃣ Add transactions
    runner.invoke(cli, ["add", "100", "Groceries", "Food", "expense", "2025-01-10"])
    runner.invoke(cli, ["add", "50", "Snacks", "Food", "expense", "2025-01-15"])

    # 3️⃣ Check budget status
    result = runner.invoke(cli, ["budget-status", "Food", "2025-01"])
    assert result.exit_code == 0
    assert "Total spent: 150" in result.output
    assert "Remaining: 150" in result.output
    assert "Consumption: 50%" in result.output
    assert "Exceeded: False" in result.output

def test_over_budget_alert():
    runner = CliRunner()

    # Add budget
    runner.invoke(cli, ["add-budget", "Transport", "2025-01", "100"])

    # Add transactions to exceed budget
    runner.invoke(cli, ["add", "120", "Taxi", "Transport", "expense", "2025-01-05"])

    # Check budget status
    result = runner.invoke(cli, ["budget-status", "Transport", "2025-01"])
    assert result.exit_code == 0
    assert "Total spent: 120" in result.output
    assert "Remaining: -20" in result.output
    assert "Consumption: 120%" in result.output
    assert "Exceeded: True" in result.output
    assert "Alert: Budget exceeded" in result.output
