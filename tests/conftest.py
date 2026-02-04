import os
import pytest
from pathlib import Path

# 1. Manually finds the project root and sets the DB path
# This ensures both the test and the app use the same 'budget.db'
BASE_DIR = Path(__file__).resolve().parent.parent
test_db_path = BASE_DIR / "data" / "budget.db"
os.environ["BUDGET_DB_PATH"] = str(test_db_path)

from budgetapp.storage.db import init_db, get_connection

@pytest.fixture(autouse=True)
def setup_db():
    init_db()  # Ensures tables exist
    conn = get_connection()
    cur = conn.cursor()
    # Wipes data so tests start fresh
    cur.execute("DELETE FROM transactions")
    cur.execute("DELETE FROM budgets")
    conn.commit()
    conn.close()