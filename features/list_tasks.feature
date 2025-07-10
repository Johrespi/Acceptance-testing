# language: en
Feature: List Tasks
  As a user, I want to view all tasks in my to-do list.

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | task          |
      | Buy groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain:
      """
      Tasks:
      - Buy groceries
      - Pay bills
      """