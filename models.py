from pydantic import BaseModel
from typing import List, Optional

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

class User(BaseModel):
    id: int
    name: str
    email: str
    tasks: List[Task] = []
