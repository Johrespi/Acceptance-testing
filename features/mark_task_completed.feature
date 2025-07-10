# language: en
Feature: Mark Task as Completed
  As a user, I want to mark tasks as completed.

  Scenario: Mark a task as completed
    Given the to-do list contains tasks with status:
      | task          | status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed