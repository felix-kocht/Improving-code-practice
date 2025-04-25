import pytest
from task import Task
from datetime import date

def test_task_creation_valid():
    task = Task('name1',date(1,3,2))
    assert task.date.year == 1
    assert task.name == "name1"
    assert task.completed == False

