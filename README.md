Johann Ramirez, Software Engineering II, July 10, 2025.

Introduction
This report details the activities performed during the Acceptance Test Workshop. The main objective was to understand and apply Behavior-Driven Development (BDD) principles using Python and the Behave framework to develop a simple To-Do List Manager application.

Development
The development process strictly adhered to the Behavior-Driven Development (BDD) cycle, focusing on six distinct features, each validated by a specific scenario. These features, encompassing the core functionalities of the To-Do List Manager, included:
1.  Adding a new task.
2.  Listing all existing tasks.
3.  Marking a task as completed.
4.  Clearing the entire list of tasks.
5.  Deleting a specific task (an added requirement).
6.  Editing the description of an existing task (an added requirement).

The procedure commenced with defining these desired behaviors through six separate feature files, each written in Gherkin syntax and dedicated to a single feature and its corresponding scenario. Subsequently, step definitions were implemented in Python using the Behave framework, linking the Gherkin steps to executable code. This initial implementation of step definitions, without the underlying application logic, led to failing tests, representing the 'red' phase of the BDD cycle. The core application logic for the To-Do List Manager was then developed iteratively within the 'main.py' file. Each method within the ToDoList class (add_task, list_tasks, mark_task_as_completed, clear_tasks, delete_task, edit_task) was meticulously implemented to satisfy the corresponding failing tests, thereby transitioning to the 'green' phase. This iterative approach ensured that the application's functionality was directly driven by and validated against the defined acceptance criteria. Finally, a simple command-line interface was integrated into 'main.py' to allow direct user interaction with the developed To-Do List Manager, demonstrating the practical application of the validated features.

Conclusions
Behavior-Driven Development proved to be an effective methodology for aligning business requirements with technical implementation. The use of Gherkin language facilitated clear communication and understanding of the system's expected behavior. The iterative process of writing failing tests and then implementing code to make them pass ensured that the application met its specified requirements.

Recommendations
For future projects, it is recommended to integrate BDD practices from the early stages of development to foster collaboration and maintain a clear understanding of requirements. Continuous testing with tools like Behave should be a standard practice to ensure software quality and prevent regressions. Further exploration of advanced Behave features, such as hooks and custom formatters, could enhance the testing process.

References
- Behave Documentation (https://behave.readthedocs.io/)