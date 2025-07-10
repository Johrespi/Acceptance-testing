# language: en
Feature: Delete Specific Task
  As a user, I want to delete a specific task from my to-do list.

  Scenario: Delete a specific task
    Given the to-do list contains tasks:
      | task          |
      | Buy groceries |
      | Learn BDD     |
    When the user deletes the task "Buy groceries"
    Then the to-do list should not contain "Buy groceries"
    And the to-do list should contain "Learn BDD"