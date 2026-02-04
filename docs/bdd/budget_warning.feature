Feature: Budget warning at 80%
  As a user
  I want to receive a warning when 80% of my budget is consumed
  So that I can avoid overspending

  Scenario: Spending reaches 80% of budget
    Given a budget "Entertainment" for "2025-01" with amount 200
    And the following transactions exist:
      | amount | category      | date       | type    |
      | 50     | Entertainment| 2025-01-05 | expense |
      | 110    | Entertainment| 2025-01-10 | expense |
    When I check the budget status
    Then the total spent should be 160
    And the remaining budget should be 40
    And a warning should be issued indicating 80% consumed
