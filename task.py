import datetime
from typing import Optional

class Task:
    def __init__(self,name: str, date: Optional[datetime.date] = None, completed: bool = False):
        self.name = name
        self.date = date
        self.completed = completed

