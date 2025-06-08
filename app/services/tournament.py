from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.tournament import TournamentCreate, PlayerRegister
from app.models.tournament import Tournament, Player
from app.repositories.tournament import TournamentRepository


async def create_tournament(
        session: AsyncSession,
        data: TournamentCreate
) -> Tournament:
    repo = TournamentRepository(session)
    tournament = Tournament(**data.dict())
    return await repo.create_tournament(tournament)


async def register_player(
        session: AsyncSession,
        tournament_id: int,
        data: PlayerRegister
) -> Player:
    repo = TournamentRepository(session)

    if not await repo.get_tournament(tournament_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tournament not found"
        )

    if await repo.is_email_registered(tournament_id, data.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    if await repo.count_players(tournament_id) >= (
            tournament := await repo.get_tournament(tournament_id)
    ).max_players:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tournament is full"
        )

    player = Player(
        name=data.name,
        email=data.email,
        tournament_id=tournament_id
    )
    return await repo.register_player(player)