import os
import pytest
from pathlib import Path
import importlib

@pytest.fixture(autouse=True)
def use_temp_db(tmp_path, monkeypatch):
    # 1. Create a unique DB file for this test run
    test_db = tmp_path / "test.db"
    monkeypatch.setenv("BUDGET_DB_PATH", str(test_db))

    # 2. Reload db.py so it picks up the new env var
    import budgetapp.storage.db as db
    importlib.reload(db)

    # 3. Initialize the DB
    db.init_db()

    # 4. Clean tables
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM transactions")
    cur.execute("DELETE FROM budgets")
    conn.commit()
    conn.close()