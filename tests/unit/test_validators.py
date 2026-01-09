import pytest
from budgetapp.utils.validators import (
    validate_amount,
    validate_date,
    validate_type,
    validate_category,
    validate_transaction,
)


# ---------- validate_amount ----------

def test_validate_amount_ok():
    validate_amount(10)
    validate_amount(-5.5)


def test_validate_amount_zero():
    with pytest.raises(ValueError):
        validate_amount(0)


def test_validate_amount_not_number():
    with pytest.raises(ValueError):
        validate_amount("abc")


# ---------- validate_date ----------

def test_validate_date_ok():
    validate_date("2025-01-01")


def test_validate_date_invalid_format():
    with pytest.raises(ValueError):
        validate_date("01-01-2025")


# ---------- validate_type ----------

def test_validate_type_ok():
    validate_type("income")
    validate_type("expense")


def test_validate_type_invalid():
    with pytest.raises(ValueError):
        validate_type("other")


# ---------- validate_category ----------

def test_validate_category_ok():
    validate_category("Food")


def test_validate_category_empty():
    with pytest.raises(ValueError):
        validate_category("")


# ---------- validate_transaction ----------

def test_validate_transaction_ok():
    data = {
        "amount": 50,
        "date": "2025-01-01",
        "type": "expense",
        "category": "Food",
    }
    validate_transaction(data)


def test_validate_transaction_missing_field():
    data = {
        "amount": 50,
        "date": "2025-01-01",
        "type": "expense",
    }
    with pytest.raises(ValueError):
        validate_transaction(data)
