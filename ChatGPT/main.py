# main.py

from fastapi import FastAPI, HTTPException
from models import Todo
from Database import Database

app = FastAPI()
data = Database()
data.connect()

@app.get("/")
async def root():
    return {"message": "Hello Anantha Narayanan"}

### GET all TODOS ###
@app.get("/todos")
async def get_todos():
    todos = data.Get_all()
    if todos is None:
        raise HTTPException(status_code=404, detail="No todos found")
    return {"todos": todos}

### CREATE A Todo ###
@app.post("/todos")
async def create_todos(todo: Todo):
    data.Insert_data(todo.item, todo.isCompleted)
    return {"message": "Todo has been added!"}

### Get Single todo ###
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    todos = data.Get_all()
    for todo in todos:
        if todo[0] == todo_id:  # Assuming ItemID is the first field
            return {"todo": {"id": todo[0], "item": todo[1], "isCompleted": todo[2]}}
    raise HTTPException(status_code=404, detail="No Todo found")

### Update Todo list ###
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: Todo):
    todos = data.Get_all()
    for todo in todos:
        if todo[0] == todo_id:  # Assuming ItemID is the first field
            data.update_data(todo_id, todo_obj.isCompleted)
            return {"message": "Todo updated successfully"}
    raise HTTPException(status_code=404, detail="No Todo found to update")

### Delete a item ###
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    todos = data.Get_all()
    for todo in todos:
        if todo[0] == todo_id:  # Assuming ItemID is the first field
            data.delete_data(todo_id)
            return {"message": "This has been deleted from ToDo list!"}
    raise HTTPException(status_code=404, detail="No Todo found")
