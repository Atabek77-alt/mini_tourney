from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tournament import Tournament, Player

class TournamentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_tournament(self, tournament: Tournament) -> Tournament:
        self.session.add(tournament)
        await self.session.commit()
        await self.session.refresh(tournament)
        return tournament

    async def get_tournament(self, tournament_id: int) -> Tournament | None:
        result = await self.session.execute(
            select(Tournament).where(Tournament.id == tournament_id)
        )
        return result.scalar_one_or_none()

    async def count_players(self, tournament_id: int) -> int:
        result = await self.session.execute(
            select(func.count(Player.id)).where(Player.tournament_id == tournament_id)
        )
        return result.scalar_one()

    async def is_email_registered(self, tournament_id: int, email: str) -> bool:
        result = await self.session.execute(
            select(Player)
            .where(Player.tournament_id == tournament_id)
            .where(Player.email == email)
        )
        return result.scalar_one_or_none() is not None

    async def register_player(self, player: Player) -> Player:
        self.session.add(player)
        await self.session.commit()
        await self.session.refresh(player)
        return player