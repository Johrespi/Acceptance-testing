# language: en
Feature: Clear All Tasks
  As a user, I want to clear all tasks from my to-do list.

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | task          |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty