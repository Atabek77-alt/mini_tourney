from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.models import Tournament, Player

class TournamentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_tournament(self, data) -> Tournament:
        tournament = Tournament(**data)
        self.session.add(tournament)
        await self.session.commit()
        return tournament

    async def register_player(self, tournament_id: int, player_data) -> Player:
        player = Player(**player_data, tournament_id=tournament_id)
        self.session.add(player)
        await self.session.commit()
        return player

    async def get_players_count(self, tournament_id: int) -> int:
        result = await self.session.execute(
            select(func.count()).where(Player.tournament_id == tournament_id)
        )
        return result.scalar()