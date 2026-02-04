Feature: Delete a transaction
  As a user
  I want to delete a transaction
  So that my budget totals are updated correctly

  Scenario: Delete an expense transaction
    Given a budget "Food" for "2025-01" with amount 300
    And the following transactions exist:
      | amount | category | date       | type    |
      | 50     | Food     | 2025-01-05 | expense |
      | 20     | Food     | 2025-01-10 | expense |
    When I delete the transaction with amount 50 on "2025-01-05"
    Then the total spent for "Food" in "2025-01" should be 20
    And the remaining budget should be 280
