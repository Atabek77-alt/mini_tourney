from fastapi import APIRouter, Depends
from app.services.tournament import TournamentService
from app.repositories.tournament import TournamentRepository
from app.db import get_db
from app.schemas import TournamentCreate, PlayerRegister

router = APIRouter(prefix="/tournaments")

@router.post("/")
async def create_tournament(data: TournamentCreate, db=Depends(get_db)):
    repo = TournamentRepository(db)
    return await repo.create_tournament(data.dict())

@router.post("/{tournament_id}/register")
async def register_player(
    tournament_id: int,
    player: PlayerRegister,
    db=Depends(get_db)
):
    repo = TournamentRepository(db)
    service = TournamentService(repo)
    return await service.register_player(tournament_id, player.dict())
