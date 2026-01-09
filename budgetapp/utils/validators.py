from datetime import datetime


def validate_amount(amount):
    if not isinstance(amount, (int, float)):
        raise ValueError("Le montant doit être un nombre.")
    if amount == 0:
        raise ValueError("Le montant ne peut pas être égal à 0.")


def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except (ValueError, TypeError):
        raise ValueError("La date doit être au format YYYY-MM-DD.")


def validate_type(transaction_type):
    if transaction_type not in ("income", "expense"):
        raise ValueError("Le type doit être 'income' ou 'expense'.")


def validate_category(category):
    if not isinstance(category, str) or not category.strip():
        raise ValueError("La catégorie doit être une chaîne non vide.")


def validate_transaction(data: dict):
    required_fields = ["amount", "date", "type", "category"]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Champ manquant : {field}")

    validate_amount(data["amount"])
    validate_date(data["date"])
    validate_type(data["type"])
    validate_category(data["category"])