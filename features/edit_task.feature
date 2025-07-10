# language: en
Feature: Edit Task Description
  As a user, I want to edit the description of an existing task.

  Scenario: Edit the description of a task
    Given the to-do list contains tasks:
      | task      |
      | Buy milk  |
    When the user edits the task "Buy milk" to "Buy almond milk"
    Then the to-do list should not contain "Buy milk"
    And the to-do list should contain "Buy almond milk"