import pytest
from budgetapp.storage.db import init_db, get_connection

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    """
    Initializes the DB before any integration test runs.
    """
    # Initialize DB tables
    init_db()
    
    # Provide a connection if needed
    conn = get_connection()
    
    # CLEAR TABLES BEFORE EACH MODULE
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions")
    cursor.execute("DELETE FROM budgets")
    conn.commit()

    yield conn
    conn.close()


