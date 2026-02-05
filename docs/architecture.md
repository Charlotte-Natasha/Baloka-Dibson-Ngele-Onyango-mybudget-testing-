**Overview**

- **Purpose:** Small CLI-based budget and transaction manager focused on recording transactions, computing budgets, and raising simple alerts when thresholds are reached.
- **Scope:** Command-line interface, business services, storage adapters, and small utility helpers.

**High-Level Architecture**

- **CLI layer:** Handles user commands and input parsing (see [budgetapp/cli/app.py] and [budgetapp/cli/commands.py]).

- **Service layer:** Core business logic lives in [budgetapp/services] — e.g., [budgetapp/services/budget_service.py] and [budgetapp/services/transaction_service.py].

- **Storage layer:** Persistence and data models under [budgetapp/storage] (database adapter [budgetapp/storage/db.py], and record modules).

- **Utilities:** Shared helpers for validation and dates in [budgetapp/utils] (for example [budgetapp/utils/validators.py]).

- **Configuration:** Global settings in [budgetapp/config.py].

**Data Flow (short)**

- User runs a command via the CLI → CLI parses and validates input → Service layer executes business rules → Service calls storage adapter to persist or fetch data → CLI displays results.

**Key Responsibilities**

- **CLI:** Present simple commands (list, add, edit, delete, export).

- **Services:** Calculate totals, remaining budgets, percentages, and generate alert messages.

- **Storage:** Provide a small, testable adapter layer so services remain decoupled from persistence.

- **Utils:** Small pure helpers for date handling and validation; easily unit-tested.

**Testing & Quality**

- Unit and integration tests live in the `tests` folder. Services and storage are covered by focused tests to keep logic verifiable (see [tests/unit] and [tests/integrations] ).

**Running & Development**

- See [README.md] for setup. Quick commands:

```bash
pip install -r requirements.txt
pytest
```
