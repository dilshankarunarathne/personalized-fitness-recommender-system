from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import main

app = FastAPI()

## CORS



app.include_router(main.router)
