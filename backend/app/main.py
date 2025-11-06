from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Allow frontend dev server access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten this later for prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Todo model
class TodoCreate(BaseModel):
    title: str
    completed: bool = False

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

# In-memory storage (replace with database in production)
todos: List[Todo] = []
next_id = 1

@app.get("/api/hello")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/api/todos", response_model=List[Todo])
def get_todos():
    return todos

@app.post("/api/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    global next_id
    new_todo = Todo(id=next_id, title=todo.title, completed=todo.completed)
    todos.append(new_todo)
    next_id += 1
    return new_todo

@app.put("/api/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_update: TodoCreate):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            updated_todo = Todo(id=todo_id, title=todo_update.title, completed=todo_update.completed)
            todos[i] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/api/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(i)
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
