import click
from budgetapp.storage.db import init_db

@click.group()
def cli():
    """BudgetPilot CLI"""
    pass

@click.command()
def init():
    """Initialize the database"""
    init_db()
    click.echo("Database initialized!")

# Placeholder commands for future use (do NOT implement functionality yet)
@click.command()
def add_transaction():
    click.echo("Add transaction command (to be implemented by Jeanette)")

@click.command()
def show_budget():
    click.echo("Show budget command (to be implemented by Emmanuel)")

cli.add_command(init)
cli.add_command(add_transaction)
cli.add_command(show_budget)

if __name__ == "__main__":
    cli()
