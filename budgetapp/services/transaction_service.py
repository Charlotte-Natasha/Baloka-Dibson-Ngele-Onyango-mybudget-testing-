from budgetapp.storage.db import get_connection
from budgetapp.storage.transactions import (
    create_transaction as db_create,
    get_transactions as db_get,
    update_transaction as db_update,
    delete_transaction as db_delete,
)
from budgetapp.utils.validators import validate_transaction


def create_transaction(data):
    validate_transaction(data)

    conn = get_connection()
    try:
        transaction_id = db_create(conn, data)
        return transaction_id
    finally:
        conn.close()


def list_transactions(filters=None):
    conn = get_connection()
    try:
        return db_get(conn, filters)
    finally:
        conn.close()


def update_transaction(transaction_id, data):
    validate_transaction(data)

    conn = get_connection()
    try:
        updated = db_update(conn, transaction_id, data)
        if updated == 0:
            raise ValueError("Transaction introuvable.")
        return updated
    finally:
        conn.close()


def delete_transaction(transaction_id):
    conn = get_connection()
    try:
        deleted = db_delete(conn, transaction_id)
        if deleted == 0:
            raise ValueError("Transaction introuvable.")
        return deleted
    finally:
        conn.close()
