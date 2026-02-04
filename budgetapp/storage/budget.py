from budgetapp.storage.db import get_connection
from budgetapp.services.budget_service import (
    calculate_total_spent,
    calculate_remaining_budget,
    calculate_consumption_percentage,
    is_budget_exceeded,
    get_budget_alert
)
from budgetapp.storage.transactions import get_transactions


# Budget operations

def create_budget(category: str, period: str, amount: float):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO budgets (category, period, amount) VALUES (?, ?, ?)",
        (category, period, amount)
    )
    conn.commit()
    conn.close()


def get_budget(category: str, period: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, category, period, amount FROM budgets WHERE category=? AND period=?",
        (category, period)
    )
    row = cur.fetchone()
    conn.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "category": row[1],
        "period": row[2],
        "amount": row[3]
    }


def list_budgets():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT category, period, amount FROM budgets ORDER BY period")
    rows = cur.fetchall()
    conn.close()

    return [
        {"category": r[0], "period": r[1], "amount": r[2]}
        for r in rows
    ]


def delete_budget(category: str, period: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM budgets WHERE category=? AND period=?",
        (category, period)
    )
    conn.commit()
    conn.close()


# Budget calculation / reporting

def get_budget_status(category: str, period: str):
    conn = get_connection()
    try:
        # 1. Fetch budget details directly to keep the connection alive
        cur = conn.cursor()
        cur.execute(
            "SELECT amount FROM budgets WHERE category=? AND period=?",
            (category, period)
        )
        budget_row = cur.fetchone()
        
        # If no budget exists, return None immediately
        if budget_row is None:
            return None
        
        budget_amount = budget_row[0]

        # 2. Fetch raw transactions using the SAME open connection
        raw_transactions = get_transactions(conn, category=category, period=period)
        
        # Ensure raw_transactions is a list, even if empty
        if raw_transactions is None:
            raw_transactions = []

        # 3. Convert tuples to dictionaries for the service functions
        transactions = [
            {
                "id": tx[0],
                "amount": tx[1],
                "date": tx[2],
                "type": tx[3],
                "category": tx[4],
                "description": tx[5]
            }
            for tx in raw_transactions
        ]

        # 4. Use your service logic for calculations
        total_spent = calculate_total_spent(transactions)
        remaining = calculate_remaining_budget(total_spent, budget_amount)
        consumption_pct = calculate_consumption_percentage(total_spent, budget_amount)
        exceeded = is_budget_exceeded(total_spent, budget_amount)
        alert = get_budget_alert(total_spent, budget_amount)

        return {
            "category": category,
            "period": period,
            "budget_amount": budget_amount,
            "total_spent": total_spent,
            "remaining": remaining,
            "consumption_pct": consumption_pct,
            "exceeded": exceeded,
            "alert": alert
        }
    finally:
        # Always close the connection, even if an error occurs
        conn.close()