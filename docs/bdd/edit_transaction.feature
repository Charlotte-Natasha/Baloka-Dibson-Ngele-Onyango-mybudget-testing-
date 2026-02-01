Feature: Edit transaction

  As a user, I want to edit an existing transaction so that I can correct mistakes in amount or category.

  Scenario: User edits the amount of an existing transaction

    Given a transaction exists with:
      | id | amount | category  | type    | date        |
      | 1  | 50     | Transport | expense | 2025-01-10  |

    And a budget of 200€ exists for category "Transport" for period "2025-01". 

    When the user updates the transaction with id 1 to have amount 30€, then the transaction amount should be updated to 30€
    and the total spent for "Transport" in "2025-01" should be 30€. 