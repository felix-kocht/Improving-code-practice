from task import Task
from typing import Optional
import datetime


def create_element(name: str, year: Optional[int] = None, month: Optional[int] = None, day: Optional[int] = None, completed: bool = False):
    try:
        if year is not None and month is not None and day is not None:
            date = datetime.date(year,month,day)
        else:
            date = None
    except:
        print("date seems to be invalid, task was not created")
        return None
    return Task(name,date,completed)