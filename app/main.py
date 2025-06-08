from fastapi import FastAPI
from app.api.tournament import router

app = FastAPI()
app.include_router(router)
