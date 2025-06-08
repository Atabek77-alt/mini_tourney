from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.schemas.tournament import (
    TournamentCreate, TournamentRead,
    PlayerRegister, PlayerRead
)
from app.services.tournament import (
    create_tournament as service_create_tournament,
    register_player as service_register_player
)

router = APIRouter()


@router.post("/tournaments", response_model=TournamentRead)
async def create_tournament_endpoint(
    tournament: TournamentCreate,
    db: AsyncSession = Depends(get_db)
):
    return await service_create_tournament(db, tournament)


@router.post("/tournaments/{tournament_id}/register", response_model=PlayerRead)
async def register_player_endpoint(
    tournament_id: int,
    player: PlayerRegister,
    db: AsyncSession = Depends(get_db)
):
    return await service_register_player(db, tournament_id, player)
