import pytest
from main import display_element
from task_manager import create_element
from main import parse_user_input


def test_parse_user_input_correct_fields():
    name, year, month, day, completed_flag = parse_user_input(
        "MyTask", "2025", "12", "24", "y")

    assert name == "MyTask"
    assert year == 2025
    assert month == 12
    assert day == 24
    assert completed_flag is True


def test_parse_user_input_empty_date_fields():
    name, year, month, day, completed_flag = parse_user_input(
        "MyTask", "", "", "", "n")

    assert name == "MyTask"
    assert year is None
    assert month is None
    assert day is None
    assert completed_flag is False

def test_display_element(capsys):
    # TODO: find out if we create these from scratch every time
    task = create_element('first_task', 2026, 4, 23, True)
    display_element(task, 4)
    captured = capsys.readouterr()
    assert "first_task" in captured.out
    assert "2026" in captured.out
    assert "x " in captured.out

