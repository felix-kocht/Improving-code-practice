import json
import os

import pytest

from file_io import load_file, save_file
from task_manager import create_element


@pytest.fixture
def sample_tasklist():
    return [
        create_element("Task 1", 2025, 12, 25, False),
        create_element("Task 2", 2024, 11, 20, True),
    ]


@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "test_tasks.json"


def test_save_file(temp_file, sample_tasklist):
    save_file(temp_file, sample_tasklist)

    assert os.path.exists(temp_file)

    with open(temp_file, "r") as file:
        content = json.load(file)

    assert len(content) == 2
    assert content[0]["name"] == "Task 1"
    assert content[0]["due_date"]["year"] == 2025
    assert content[0]["completed"] is False
    assert content[1]["name"] == "Task 2"
    assert content[1]["due_date"]["year"] == 2024
    assert content[1]["completed"] is True


def test_load_file(temp_file, sample_tasklist):
    # Save the sample tasklist to the temp file
    save_file(temp_file, sample_tasklist)

    # Load the tasklist back from the file
    loaded_tasklist = load_file(temp_file)

    assert len(loaded_tasklist) == 2
    assert loaded_tasklist[0].name == "Task 1"
    assert loaded_tasklist[0].date.year == 2025
    assert loaded_tasklist[0].completed is False
    assert loaded_tasklist[1].name == "Task 2"
    assert loaded_tasklist[1].date.year == 2024
    assert loaded_tasklist[1].completed is True


def test_load_file_nonexistent():
    tasklist = load_file("nonexistent_file.json")
    assert tasklist == []
