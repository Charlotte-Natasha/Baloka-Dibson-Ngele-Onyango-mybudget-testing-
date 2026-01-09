def create_transaction(conn, data):
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO transactions (amount, date, type, category)
        VALUES (?, ?, ?, ?)
        """,
        (data["amount"], data["date"], data["type"], data["category"])
    )
    conn.commit()
    return cursor.lastrowid


def get_transactions(conn, filters=None):
    cursor = conn.cursor()
    query = "SELECT id, amount, date, type, category FROM transactions"
    params = []

    if filters:
        clauses = []
        for key, value in filters.items():
            clauses.append(f"{key} = ?")
            params.append(value)
        query += " WHERE " + " AND ".join(clauses)

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