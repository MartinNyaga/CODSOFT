# A TO-DO LIST CLI APP

#### TASK 1

## Description
The Todo List CLI App is a simple command-line interface (CLI) application designed to help users manage their tasks in a straightforward and efficient manner. The app allows users to add, list, delete, update, and mark tasks as complete, providing a convenient way to organize their to-do lists from the command line.

## Features
- Add Task: Easily add new tasks to the list, providing a name, description, and due date for better task organization.
- List Tasks: View all tasks in the to-do list with relevant details, including task name, completion status, and due date.
- Update Task: Modify existing tasks by updating the name, description, and due date, ensuring flexibility in managing changing priorities.
- Delete Task: Remove a task from the list as some tasks are no longer relevant.
- Complete Task: Mark a task as complete, providing a sense of accomplishment as items are checked off the to-do list.

### How to run code
- Git clone repo to your local
- Open directory to file location
- Move to lib directory
- Run python3 main.py on your terminal to see available commands
- Run python3 main.py followed by required command for execution i.e
  ```bash
  python3 main.py list-tasks 

## CLI COMMANDS 

- HELP
  ```bash
  --help   Show This message and exit

- Add Task
  ```bash
  add_task     Add a new task to the database.

- List Tasks
  ```bash
  list_task          List Tasks from the database.

- Delete Tasks
  ```bash
  delete_task         Delete Task from the database.

- Update Tasks
  ```bash
  update_task  Update a Task from the database.

- Complete a Task
  ```bash
  complete_task       To complete a Task.


## Examples on execution

- Lets Add a Task
  ```bash
  python3 main.py add_task --todo_name "cinema" --description "binge movies" --due_date "2024-9-11"

- Lets List The Number of Tasks
  ```bash
  python3 main.py list_task

- Lets Delete a Task
  ```bash
  python3 main.py delete_task 3

- Lets Update a Task
  ```bash
  python3 main.py update_task --id 2 --todo_name "cinema" --description "binge movies" --due_date "2024-9-11"

- Lets Complete a Task
  ```bash
  python3 main.py complete_task 2


## Setup Requirements

- Git
- Code editor of choice
- Github



## Technologies Used

The following have been used on this project:

- Python
- sqlalchemy

## Known Bugs

No known bugs at the moment

