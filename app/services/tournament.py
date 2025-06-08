from fastapi import HTTPException, status
from app.repositories.tournament import TournamentRepository


class TournamentService:
    def __init__(self, repository: TournamentRepository):
        self.repository = repository

    async def register_player(self, tournament_id: int, player_data):
        current_players = await self.repository.get_players_count(tournament_id)
        tournament = await self.repository.get_tournament(tournament_id)

        if current_players >= tournament.max_players:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Tournament is full"
            )
        return await self.repository.register_player(tournament_id, player_data)