import click
from budgetapp.cli.commands import add_budget, add_transaction, budget_status

@click.group()
def cli():
    """Main CLI entry point."""
    pass

# Register commands
cli.add_command(add_budget)
cli.add_command(add_transaction)
cli.add_command(budget_status)