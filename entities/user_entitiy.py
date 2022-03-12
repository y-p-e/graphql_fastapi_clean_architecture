from typing import List

from pydantic import BaseModel
import strawberry
from strawberry import ID, auto


class UserFilter(BaseModel):
    user_id: int


class TaskBaseModel(BaseModel):
    id: int
    title: str
    status: str
    user_id: int

    class Config:
        orm_mode = True


class UserBaseModel(BaseModel):
    id: int
    user_name: str
    email: str
    tasks: List[TaskBaseModel] = []

    class Config:
        orm_mode = True


@strawberry.experimental.pydantic.type(model=TaskBaseModel)
class TaskType:
    id: ID
    title: str
    status: str
    user_id: int


@strawberry.experimental.pydantic.type(model=UserBaseModel)
class UserType:
    id: ID
    user_name: auto
    email: auto
    tasks: auto
