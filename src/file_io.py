import json
import os

from task_manager import add_element, create_element


def load_file(file_path):
    """
    Load a file, convert dict to task objects, append to tasklist and return tasklist.

    :param file_path: Path to the file
    :return: Content of the file
    """
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return []

    with open(file_path, "r") as file:
        content = json.load(file)

    tasklist = []
    for task_data in content:
        task = create_element(
            name=task_data["name"],
            year=task_data["due_date"]["year"],
            month=task_data["due_date"]["month"],
            day=task_data["due_date"]["day"],
            completed=task_data["completed"],
        )
        add_element(task, tasklist)

    return tasklist


def save_file(file_path, tasklist):
    """
    Converts tasks to dict, saves content to a file.

    :param file_path: Path to the file
    :param tasklist: list of task objects to save
    """
    content = []
    for task in tasklist:
        task_data = {
            "name": task.name,
            "due_date": {
                "year": task.date.year,
                "month": task.date.month,
                "day": task.date.day,
            },
            "completed": task.completed,
        }
        content.append(task_data)

    with open(file_path, "w") as file:
        json.dump(content, file, indent=4)
