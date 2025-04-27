import pytest

from src.task_manager import add_element, create_element


def test_create_element_valid():
    task = create_element("first_task", 2026, 4, 23)
    assert task.name == "first_task"
    assert task.date.year == 2026
    assert task.completed is False


def test_create_element_briefly():
    task = create_element("first_task")
    assert task.name == "first_task"
    assert task.date is None
    assert task.completed is False


def test_create_element_invalid():
    with pytest.raises(ValueError) as exc_info:
        create_element("bad_task", 2024, 2, 30)
    assert "invalid" in str(exc_info.value).lower()


def test_add_element():
    tasklist = []
    task = create_element("new_task", 2025, 12, 25)
    add_element(task, tasklist)
    assert len(tasklist) == 1
    assert tasklist[0].name == "new_task"
    assert tasklist[0].date.year == 2025
    assert tasklist[0].completed is False
