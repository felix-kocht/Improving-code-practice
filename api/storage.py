from .database import get_connection
from .models import Task

# def load_tasklist(tasks: list[Task]):
#     """
#     Loads the tasklist from a list of tasks.
#     """
#     global tasklist
#     tasklist = tasks


def add_task(task: Task):
    """
    Adds a task to the storage.
    """
    # tasklist.append(task)
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO tasks (name, date, completed) VALUES (?, ?, ?)",
            (task.name, task.date.isoformat() if task.date else None, task.completed),
        )


def get_all_tasks():
    """
    Retrieves all tasks from the storage.
    """
    # return tasklist
    with get_connection() as conn:
        cursor = conn.execute("SELECT id, name, date, completed FROM tasks")
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            task = Task(
                name=row[1], date=row[2] if row[2] else None, completed=bool(row[3])
            )
            tasks.append(task)
        return tasks
