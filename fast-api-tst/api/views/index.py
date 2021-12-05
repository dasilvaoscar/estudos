from fastapi import APIRouter
from .models import User

router = APIRouter(
  responses={404: {"description": "Not found"}},
)

@router.get('/')
def index():
  return {"message": "Hello World"}

@router.post('/users')
def user(user: User):
  return user.dict()