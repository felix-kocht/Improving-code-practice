import datetime
from typing import Optional

from task import Task


def create_element(
    name: str,
    year: Optional[int] = None,
    month: Optional[int] = None,
    day: Optional[int] = None,
    completed: bool = False,
):
    try:
        if year is not None and month is not None and day is not None:
            date = datetime.date(year, month, day)
        else:
            date = None
    except ValueError as e:
        raise ValueError("date seems to be invalid, task was not created") from e
    return Task(name=name, date=date, completed=completed)


def add_element(element: Task, tasklist: list):
    if element is not None:
        tasklist.append(element)
