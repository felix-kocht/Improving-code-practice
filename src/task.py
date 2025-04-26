import datetime
from typing import Optional


class Task:
    def __init__(
        self, name: str, date: Optional[datetime.date] = None, completed: bool = False
    ):
        self.name = name
        self.date = date
        self.completed = completed

    def __str__(self):
        if self.completed:
            checked_symbol = "x"
        else:
            checked_symbol = "o"
        date_str = self.date.strftime("%Y-%m-%d") if self.date else "No due date"
        return f"{checked_symbol} {self.name}, due: {date_str}"
