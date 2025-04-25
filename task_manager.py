import datetime
from task import Task
from typing import Optional


def create_element(name: str, year: Optional[int] = None, month: Optional[int] = None, day: Optional[int] = None, completed: bool = False):
    try:
        if year is not None and month is not None and day is not None:
            date = datetime.date(year,month,day)
        else:
            date = None
    except ValueError as e:
        raise ValueError("date seems to be invalid, task was not created") from e
    return Task(name,date,completed)

def add_element(element: Task):
    pass

def display_element(element: Task, number: int):
    if element.completed:
        checked_symbol = "x"
    else:
        checked_symbol = "o"
    print(f"No." + number + ": " + element.name + " " + checked_symbol + " due" + element.date)