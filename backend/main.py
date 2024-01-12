from fastapi import FastAPI
from routes import main

app = FastAPI()

app.include_router(main.router)
