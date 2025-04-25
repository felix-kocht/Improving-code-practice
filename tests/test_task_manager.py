import pytest
from task_manager import create_element, add_element, display_element

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
    with pytest.raises(ValueError) as exc_info:
        create_element("bad_task", 2024, 2, 30)
    assert "invalid" in str(exc_info.value).lower()


def test_display_element(capsys):
    task = create_element('first_task', 2026, 4, 23) #TODO: find out if we create these from scratch every time
    display_element(task, 4)
    captured = capsys.readouterr()
    assert "first_task" in captured.out
    assert "2026" in captured.out
    
