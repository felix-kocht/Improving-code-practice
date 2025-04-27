import datetime
from typing import Optional

from pydantic import BaseModel


class Task(BaseModel):
    """
    A class representing a task with a name, due date, and completion status.
    """

    name: str
    date: Optional[datetime.date] = None
    completed: bool = False

    def __str__(self):
        if self.completed:
            checked_symbol = "x"
        else:
            checked_symbol = "o"
        date_str = self.date.strftime("%Y-%m-%d") if self.date else "No due date"
        return f"{checked_symbol} {self.name}, due: {date_str}"
