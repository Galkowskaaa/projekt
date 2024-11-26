from fastapi import FastAPI, HTTPException
from models import User, Task
from crud import create_user, get_user, update_user, delete_user

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hej, dodaj /docs do linku :>"}

@app.post("/users/", response_model=User)
def api_create_user(user: User):
    return create_user(user)

@app.get("/users/{user_id}", response_model=User)
def api_get_user(user_id: int):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Użytkownik nie znaleziony")
    return user

@app.put("/users/{user_id}", response_model=User)
def api_update_user(user_id: int, updated_user: User):
    user = update_user(user_id, updated_user)
    if not user:
        raise HTTPException(status_code=404, detail="Użytkownik nie znaleziony")
    return user

@app.delete("/users/{user_id}")
def api_delete_user(user_id: int):
    if not delete_user(user_id):
        raise HTTPException(status_code=404, detail="Użytkownik nie znaleziony")
    return {"detail": "Użytkownik usunięty"}
