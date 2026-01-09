import pytest
from unittest.mock import patch, MagicMock

from budgetapp.services.transaction_service import (
    create_transaction,
    list_transactions,
    update_transaction,
    delete_transaction,
)

VALID_TRANSACTION = {
    "amount": 100,
    "date": "2025-01-01",
    "type": "income",
    "category": "Salary",
}

# ---------- create_transaction ----------

@patch("budgetapp.services.transaction_service.db_create")
@patch("budgetapp.services.transaction_service.get_connection")
def test_create_transaction_ok(mock_get_conn, mock_db_create):
    mock_conn = MagicMock()
    mock_get_conn.return_value = mock_conn
    mock_db_create.return_value = 1

    transaction_id = create_transaction(VALID_TRANSACTION)

    assert transaction_id == 1
    mock_db_create.assert_called_once()
    mock_conn.close.assert_called_once()


def test_create_transaction_invalid():
    invalid_data = {
        "amount": 0,
        "date": "2025-01-01",
        "type": "income",
        "category": "Salary",
    }

    with pytest.raises(ValueError):
        create_transaction(invalid_data)


# ---------- list_transactions ----------

@patch("budgetapp.services.transaction_service.db_get")
@patch("budgetapp.services.transaction_service.get_connection")
def test_list_transactions(mock_get_conn, mock_db_get):
    mock_conn = MagicMock()
    mock_get_conn.return_value = mock_conn
    mock_db_get.return_value = []

    result = list_transactions()

    assert result == []
    mock_conn.close.assert_called_once()


# ---------- update_transaction ----------

@patch("budgetapp.services.transaction_service.db_update")
@patch("budgetapp.services.transaction_service.get_connection")
def test_update_transaction_ok(mock_get_conn, mock_db_update):
    mock_conn = MagicMock()
    mock_get_conn.return_value = mock_conn
    mock_db_update.return_value = 1

    updated = update_transaction(1, VALID_TRANSACTION)

    assert updated == 1
    mock_conn.close.assert_called_once()


@patch("budgetapp.services.transaction_service.db_update")
@patch("budgetapp.services.transaction_service.get_connection")
def test_update_transaction_not_found(mock_get_conn, mock_db_update):
    mock_conn = MagicMock()
    mock_get_conn.return_value = mock_conn
    mock_db_update.return_value = 0

    with pytest.raises(ValueError):
        update_transaction(999, VALID_TRANSACTION)


# ---------- delete_transaction ----------

@patch("budgetapp.services.transaction_service.db_delete")
@patch("budgetapp.services.transaction_service.get_connection")
def test_delete_transaction_ok(mock_get_conn, mock_db_delete):
    mock_conn = MagicMock()
    mock_get_conn.return_value = mock_conn
    mock_db_delete.return_value = 1

    deleted = delete_transaction(1)

    assert deleted == 1
    mock_conn.close.assert_called_once()


@patch("budgetapp.services.transaction_service.db_delete")
@patch("budgetapp.services.transaction_service.get_connection")
def test_delete_transaction_not_found(mock_get_conn, mock_db_delete):
    mock_conn = MagicMock()
    mock_get_conn.return_value = mock_conn
    mock_db_delete.return_value = 0

    with pytest.raises(ValueError):
        delete_transaction(999)
