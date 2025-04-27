from datetime import date

from task import Task


def test_task_creation_valid():
    task = Task(name="name1", date=date(1, 3, 2))
    assert task.date.year == 1
    assert task.name == "name1"
    assert task.completed is False
