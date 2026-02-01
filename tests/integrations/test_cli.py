import pytest
from click.testing import CliRunner
from budgetapp.cli.app import cli  
from budgetapp.storage.db import init_db

@pytest.fixture(autouse=True)
def setup():
    # Initialize DB for CLI tests
    init_db()

def test_add_transaction_and_check_budget():
    runner = CliRunner()

    # 1️⃣ Add a budget via CLI command
    result = runner.invoke(cli, ["add-budget", "Food", "2025-01", "300"])
    assert result.exit_code == 0
    assert "Budget created" in result.output

    # 2️⃣ Add transactions via CLI
    runner.invoke(cli, ["add", "100", "Groceries", "Food", "expense", "2025-01-10"])
    runner.invoke(cli, ["add", "50", "Snacks", "Food", "expense", "2025-01-15"])

    # 3️⃣ Check budget status via CLI
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
    assert "Alert" in result.output
