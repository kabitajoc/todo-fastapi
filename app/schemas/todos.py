from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    description: str | None = None


class TodoResponse(TodoCreate):
    id: int
    completed: bool = False
