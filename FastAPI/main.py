
from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Anantha Narayanan"}

todos=[]

### GET all TODOS ##

@app.get("/todos")
async def get_todos():
    return {"todos":todos}


### CREATE A Todo ###

@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message":"Todo has been added!"}


### Get Single todo ###

@app.get("/todos/{todo_id}")
async def get_todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return {"todo":todo}

    return {"Message":"No Todo is found!"}

#### Update Todo list ###
@app.put("/todos/{todo_id}")
async def update_todo(todo_id:int,todo_obj:Todo):
    for todo in todos:
        if todo.id==todo_id:
            todo.id=todo.id
            todo.item=todo_obj.item
            return {"todo":todo}

    return {"Message":"No Todo is found to Update!"}



### Delete a item ###
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            todos.remove(todo)
            return {"message":"This has been DELETED from ToDo list!"}

    return {"Message":"No Todo is found!"}
