from fastapi import FastAPI  # type: ignore
from fastapi.middleware.cors import CORSMiddleware

from .file_io import load_file, save_file
from .models import Task
from .storage import add_task, get_all_tasks, load_tasklist

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In dev, allow all. Later, you can restrict this.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    """
    Actions to perform on server startup.
    """
    tasks = load_file("data/tasklist_data.json")
    load_tasklist(tasks)


@app.on_event("shutdown")
def shutdown_event():
    """
    Actions to perform on server shutdown.
    """
    tasks = get_all_tasks()
    save_file("data/tasklist_data.json", tasks)


@app.post("/tasks")
def create_task(task: Task):
    """
    Endpoint to create a new task.
    """
    add_task(task)
    return {"message": "Task added successfully"}


@app.get("/tasks")
def read_tasks():
    """
    Endpoint to retrieve all tasks.
    """
    tasks = get_all_tasks()
    return tasks
