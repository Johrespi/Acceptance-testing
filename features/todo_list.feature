# language: en
Feature: To-Do List Manager

  As a user, I want to manage a list of tasks to keep myself organized.

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

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

  Scenario: Mark a task as completed
    Given the to-do list contains tasks with status:
      | task          | status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | task          |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Delete a specific task
    Given the to-do list contains tasks:
      | task          |
      | Buy groceries |
      | Learn BDD     |
    When the user deletes the task "Buy groceries"
    Then the to-do list should not contain "Buy groceries"
    And the to-do list should contain "Learn BDD"

  Scenario: Edit the description of a task
    Given the to-do list contains tasks:
      | task      |
      | Buy milk  |
    When the user edits the task "Buy milk" to "Buy almond milk"
    Then the to-do list should not contain "Buy milk"
    And the to-do list should contain "Buy almond milk"
