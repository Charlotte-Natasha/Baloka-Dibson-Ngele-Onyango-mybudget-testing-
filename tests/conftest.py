# tests/conftest.py
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
    yield conn
    
    # Close connection after tests
    conn.close()
