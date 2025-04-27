from fastapi import FastAPI  # type: ignore

from .models import Task
from .storage import add_task, get_all_tasks

app = FastAPI()


@app.post("/tasks")
def create_task(task: Task):
    """
    Endpoint to create a new task.
    """
    add_task(task)
    return {"message": "Task created successfully"}


@app.get("/tasks")
def read_tasks():
    """
    Endpoint to retrieve all tasks.
    """
    tasks = get_all_tasks()
    return tasks
