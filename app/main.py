from fastapi import FastAPI
from app.api.tournament import router as tournament_router

app = FastAPI(title="Mini Tournament System")

app.include_router(tournament_router, prefix="/tournaments")
