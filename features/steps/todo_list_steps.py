from behave import given, when, then
from main import ToDoList

# Helper function to find a task, as we'll do it often
def find_task(todo_list, task_name):
    return any(t["task"] == task_name for t in todo_list.tasks)

@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = ToDoList()

@when('the user adds a task "{task}"')
def step_impl(context, task):
    context.todo_list.add_task(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    assert find_task(context.todo_list, task), f'Task "{task}" not found'

@given('the to-do list contains tasks')
def step_impl(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(row['task'])

@when('the user lists all tasks')
def step_impl(context):
    context.output = context.todo_list.list_tasks()

@then('the output should contain')
def step_impl(context):
    # We check if the expected text block is a subset of the actual output
    assert context.text.strip() in context.output.strip(), f'Expected "{context.text.strip()}" not in "{context.output.strip()}"'

@given('the to-do list contains tasks with status')
def step_impl(context):
    context.todo_list = ToDoList()
    for row in context.table:
        # We assume add_task sets status to Pending by default
        context.todo_list.add_task(row['task'])

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    context.todo_list.mark_task_as_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    task_obj = next((t for t in context.todo_list.tasks if t["task"] == task), None)
    assert task_obj and task_obj["status"] == "Completed", f'Task "{task}" not completed'

@when('the user clears the to-do list')
def step_impl(context):
    context.todo_list.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo_list.tasks) == 0, "To-do list is not empty"

@when('the user deletes the task "{task}"')
def step_impl(context, task):
    context.todo_list.delete_task(task)

@then('the to-do list should not contain "{task}"')
def step_impl(context, task):
    assert not find_task(context.todo_list, task), f'Task "{task}" was found'

@when('the user edits the task "{old_task}" to "{new_task}"')
def step_impl(context, old_task, new_task):
    context.todo_list.edit_task(old_task, new_task)