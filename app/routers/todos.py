from fastapi import APIRouter, HTTPException
from app.schemas.todos import TodoCreate, TodoResponse

router = APIRouter()
todos = []
current_id = 0


@router.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate):
    global current_id
    current_id += 1
    new_todo = TodoResponse(**todo.dict(), id=current_id)
    todos.append(new_todo)
    return new_todo


@router.get("/todos", response_model=list[TodoResponse])
def get_todos():
    return todos


# Add other CRUD endpoints (GET by ID, UPDATE, DELETE)
