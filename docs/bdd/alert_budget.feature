Feature: Budget exceeded alert
  As a user,
  I want to be alerted when my expenses exceed a budget,
  So that I can better control my spending.

  Scenario: Alert is triggered when expenses exceed the budget
    Given a budget of 300€ exists for category "Food" for period "2025-01"
    And the following expenses exist for "Food" in "2025-01":
      | amount | description |
      | 200    | Groceries   |
      | 90     | Snacks      |
    When a new expense of 20€ is added for "Food" on "2025-01-20"
    Then the total spent should be 310€
    And the remaining budget should be -10€
    And the consumption percentage should be 103%
    And an alert message should be displayed