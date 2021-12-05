from fastapi import FastAPI
from api.app import init_application

app = FastAPI()

init_application(app)