from typing import List

from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    status: str
    user_id: int

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    user_name: str
    email: str
    tasks: List[Task] = []

    class Config:
        orm_mode = True
