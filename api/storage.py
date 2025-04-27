from .models import Task


def load_tasklist(tasks: list[Task]):
    """
    Loads the tasklist from a list of tasks.
    """
    global tasklist
    tasklist = tasks


def add_task(task: Task):
    """
    Adds a task to the storage.
    """
    tasklist.append(task)


def get_all_tasks():
    """
    Retrieves all tasks from the storage.
    """
    return tasklist
