from budgetapp.storage.db import get_connection

def create_transaction(conn, data):
    if conn is None:
        conn = get_connection()
        
    cursor = conn.cursor()

    description = data.get("description", "")

    cursor.execute(
        """
        INSERT INTO transactions (amount, date, type, category, description)
        VALUES (?, ?, ?, ?, ?)
        """,
        (data["amount"], data["date"], data["type"], data["category"], description)
    )
    conn.commit()
    return cursor.lastrowid


def get_transactions(conn, category=None, start_date=None, end_date=None, period=None):
    cursor = conn.cursor()

    query = "SELECT id, amount, date, type, category, description FROM transactions WHERE 1=1"
    params = []

    if category:
        query += " AND category = ?"
        params.append(category)

    if start_date:
        query += " AND date >= ?"
        params.append(start_date)

    if end_date:
        query += " AND date <= ?"
        params.append(end_date)

    cursor.execute(query, params)
    return cursor.fetchall()


def update_transaction(conn, transaction_id, data):
    cursor = conn.cursor()
    fields = []
    params = []

    for key, value in data.items():
        fields.append(f"{key} = ?")
        params.append(value)

    if not fields:
        return 0

    params.append(transaction_id)

    cursor.execute(
        f"""
        UPDATE transactions
        SET {", ".join(fields)}
        WHERE id = ?
        """,
        params
    )
    conn.commit()
    return cursor.rowcount


def delete_transaction(conn, transaction_id):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM transactions WHERE id = ?",
        (transaction_id,)
    )
    conn.commit()
    return cursor.rowcount