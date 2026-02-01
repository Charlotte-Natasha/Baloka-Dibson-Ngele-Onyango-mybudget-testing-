Feature: Export transactions

  As a user, I want to export my transactions so that I can keep a record outside the application.

  Scenario: Export all transactions to a CSV file

    Given the following transactions exist:

      | amount | description | category | type    | date        |
      | 50     | Groceries   | Food     | expense | 2025-01-10  |
      | 20     | Bus ticket  | Transport| expense | 2025-01-12  |

    When the user exports all transactions to a CSV file then a CSV file should be generated and the CSV file should contain the following rows:
    
      | amount | description | category | type    | date        |
      | 50     | Groceries   | Food     | expense | 2025-01-10  |
      | 20     | Bus ticket  | Transport| expense | 2025-01-12  |