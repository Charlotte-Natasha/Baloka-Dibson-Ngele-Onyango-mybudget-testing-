# Budget Personnel

A command-line application for personal budget management. Track expenses, manage budgets, and monitor spending with an intuitive CLI interface.

## Features

- 💰 **Budget Management** - Create and manage personal budgets
- 📊 **Transaction Tracking** - Log and categorize expenses
- 📈 **Budget Status** - View spending status and consumption percentages
- ⚠️ **Budget Alerts** - Get notified when approaching budget limits
- 📋 **CSV Export** - Export transactions to CSV for analysis
- 🧪 **Comprehensive Testing** - Unit and integration tests with BDD features

## Project Structure

```
budgetapp/
├── cli/              # Command-line interface
├── services/         # Business logic layer
├── storage/          # Data persistence
├── utils/            # Utilities (dates, validators)
└── __init__.py

tests/
├── unit/             # Unit tests
└── integrations/     # Integration tests

docs/
├── architecture.md   # Architecture documentation
└── bdd/              # BDD feature files
```

## Architecture

The application follows a **layered architecture**:

- **CLI Layer** (`cli/`) - Handles user interaction through command-line commands
- **Service Layer** (`services/`) - Contains all business logic (budget calculations, percentages, alerts)
- **Storage Layer** (`storage/`) - Manages data persistence and database operations

This separation ensures the business logic is decoupled from data access, making the code easy to test and maintain.

## Installation

### Prerequisites

- Python 3.x
- pip

### Setup

1. Clone or download the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Available Commands

#### Add a Budget

```bash
python -m budgetapp.cli.app add-budget --name "Groceries" --amount 500
```

#### Log a Transaction

```bash
python -m budgetapp.cli.app add-transaction --budget-id 1 --amount 50.00 --description "Weekly shopping"
```

#### View Budget Status

```bash
python -m budgetapp.cli.app budget-status --budget-id 1
```

## Dependencies

- **click** - Command-line interface framework
- **pytest** - Testing framework

See [requirements.txt] for full list.

## Testing

### Run All Tests

```bash
pytest
```

### Run Unit Tests

```bash
pytest tests/unit/
```

### Run Integration Tests

```bash
pytest tests/integrations/
```

### Run Tests with Coverage

```bash
pytest --cov=budgetapp
```

## Features in Development

The following features are defined in BDD format:

- **Alert Budget** - Budget limit alerts
- **Edit Transaction** - Modify existing transactions
- **Export CSV** - Export budget data to CSV format

See [docs/bdd/] for feature specifications.

## Configuration

Configuration settings can be found in [budgetapp/config.py].

## Documentation

- [Architecture] - Detailed system architecture
- [BDD Features] - Feature specifications

## Contributing

When contributing to this project:

1. Write tests for new features
2. Ensure all tests pass
3. Follow the existing code structure and style
4. Update documentation as needed

