import click
from budgetapp.storage.db import init_db, get_connection
from budgetapp.storage.transactions import create_transaction
from budgetapp.storage.budget import create_budget, get_budget_status


# Database initialization

@click.command(name="init")
def init_cmd():
    """Initialize the database."""
    init_db()
    click.echo("Database initialized!")

# Add budget

@click.command(name="add-budget")
@click.argument("category")
@click.argument("period")
@click.argument("amount", type=float)
def add_budget(category, period, amount):
    """Add a budget for a category and period."""
    init_db()  # ensure DB exists
    create_budget(category, period, amount)
    click.echo("Budget created")

# Add transaction

@click.command(name="add")
@click.argument("amount", type=float)
@click.argument("description")
@click.argument("category")
@click.argument("type")
@click.argument("date")
def add_transaction(amount, description, category, type, date):
    """Add a transaction."""
    init_db()  # ensure DB exists
    conn = get_connection()
    create_transaction(conn, {
        "amount": amount,
        "description": description,
        "category": category,
        "type": type,
        "date": date
    })
    conn.close()
    click.echo("Transaction added")

# Budget status

@click.command(name="budget-status")
@click.argument("category")
@click.argument("period")
def budget_status(category, period):
    """Show budget status for a category and period."""
    init_db()  # ensure DB exists
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
