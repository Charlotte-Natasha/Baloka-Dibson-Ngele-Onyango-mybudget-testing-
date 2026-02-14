import sqlite3
from pathlib import Path
import os

# Determine project root (3 levels up from this file)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Default DB path inside project_root/data/
DEFAULT_DB_PATH = BASE_DIR / "data" / "budget.db"

# Allow override via environment variable (for pytest)
DB_PATH = Path(os.getenv("BUDGET_DB_PATH", DEFAULT_DB_PATH)).resolve()


def set_db_path(path):
    global DB_PATH
    DB_PATH = Path(path)


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(str(DB_PATH))


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        description TEXT NOT NULL,
        category TEXT NOT NULL,
        type TEXT NOT NULL,
        date TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS budgets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        period TEXT NOT NULL,
        amount REAL NOT NULL
    )
    """)

    conn.commit()
    conn.close()