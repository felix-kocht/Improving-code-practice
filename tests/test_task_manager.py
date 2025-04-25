import pytest
from task_manager import create_element

def test_create_element_valid():
    task = create_element('first_task',2026,4,23)
    assert task.name == 'first_task'
    assert task.date.year == 2026
    assert task.completed is False


def test_create_element_briefly():
    task = create_element('first_task')
    assert task.name == 'first_task'
    assert task.date == None
    assert task.completed is False


def test_create_element_invalid():
    task = create_element('second_task', 0, 0, 0)
    assert task == None
