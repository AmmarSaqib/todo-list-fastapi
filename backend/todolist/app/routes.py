"""Application routes"""
from fastapi import Depends, APIRouter, Response
from sqlalchemy.orm import Session

import app.schemas as schemas
from app.config import Base, SessionLocal, engine

from utils.TodoListManager import TodoListManager

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.get('/')
def hello_world():
    return "Hello, World"

@router.post('/insertListItem', response_model=schemas.Todo)
def insert_list_item(todo_content: schemas.TodoCreate, response: Response, db: Session = Depends(get_db)):
    status, message = TodoListManager().insert_list_item(db, todo_content)
    response.status_code = status
    return message

@router.get('/fetchListItems', response_model=schemas.TodoFetch)
def fetch_list_items(response: Response, db: Session = Depends(get_db)):
    status, message = TodoListManager().fetch_todo_items(db)
    response.status_code = status
    return message