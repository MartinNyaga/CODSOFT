import fire
from models import session, Todo
from datetime import datetime, date

class CLI:
    def __init__(self):
        pass

    def add_task(self, todo_name, description, due_date):
        """Add a new Todo Task"""
        now = datetime.utcnow()

        finish_date = datetime.strptime(due_date, '%Y-%m-%d').date()

        task = Todo(todo_name=todo_name, due_date=finish_date, description=description, completed=False, created_at=now, updated_at=now)
        session.add(task)
        session.commit()
        print(f'Task {task} added to the database.')

    def list_task(self):
        """List all Todo Tasks"""
        tasks = session.query(Todo).all()

        if tasks:
            print("List of all Tasks:")
            for task in tasks:
                print(f"Task ID: {task.id}")
                print(f"Task: {task.todo_name}")
                print(f"Description: {task.description}")
                print(f"Due Date: {task.due_date}")
                print(f"Completed: {task.completed}")
                print(f"Created at: {task.created_at}")
                print(f"Updated at: {task.updated_at} \n")

        else:
            print("No Task Found")
                


if __name__ == '__main__':
    fire.Fire(CLI)