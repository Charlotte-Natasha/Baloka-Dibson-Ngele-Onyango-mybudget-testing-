import click
from budgetapp.storage.db import init_db
from budgetapp.storage.transactions import create_transaction
from budgetapp.storage.budget import create_budget, get_budget_status

# ---------------------------
# Database initialization
# ---------------------------
@click.command(name="init")
def init_cmd():
    init_db()
    click.echo("Database initialized!")

# ---------------------------
# Add budget
# ---------------------------
@click.command(name="add-budget")
@click.argument("category")
@click.argument("period")
@click.argument("amount", type=float)
def add_budget(category, period, amount):
    create_budget(category, period, amount)
    click.echo("Budget created")

# ---------------------------
# Add transaction
# ---------------------------
@click.command(name="add")
@click.argument("amount", type=float)
@click.argument("description")
@click.argument("category")
@click.argument("type")
@click.argument("date")
def add_transaction(amount, description, category, type, date):
    create_transaction(None, {
        "amount": amount,
        "description": description,
        "category": category,
        "type": type,
        "date": date
    })
    click.echo("Transaction added")

# ---------------------------
# Budget status
# ---------------------------
@click.command(name="budget-status")
@click.argument("category")
@click.argument("period")
def budget_status(category, period):
    status = get_budget_status(category, period)
    if not status:
        click.echo("No budget found")
        return

    click.echo(f"Total spent: {status['total_spent']}")
    click.echo(f"Remaining: {status['remaining']}")
    click.echo(f"Consumption: {status['consumption_pct']}%")
    click.echo(f"Exceeded: {status['exceeded']}")
    if status["alert"]:
        click.echo(f"Alert: {status['alert']}")