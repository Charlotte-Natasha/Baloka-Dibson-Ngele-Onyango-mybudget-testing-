from pathlib import Path

# Path to the SQLite DB
DB_PATH = Path("data/budget.db")

# Categories (optional, for validation)
CATEGORIES = [
    "Food",
    "Transport",
    "Entertainment",
    "Housing",
    "Health",
    "Other"
]

# Alert thresholds
BUDGET_WARNING_THRESHOLD = 80  # percent
BUDGET_EXCEEDED_THRESHOLD = 100  # percent
