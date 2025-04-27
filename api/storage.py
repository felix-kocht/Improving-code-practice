from .models import Task

tasklist = []


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
