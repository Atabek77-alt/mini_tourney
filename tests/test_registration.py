import pytest
from httpx import AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_full_flow():
    async with AsyncClient(app=app, base_url="http://test") as client:
        tournament_data = {
            "name": "Mini Tourney",
            "max_players": 16,
            "start_at": "2025-06-10T18:00:00"
        }
        response = await client.post("/tournaments", json=tournament_data)
        assert response.status_code == 200, f"Ошибка: {response.json()}"

        tournament_id = response.json()["id"]
        player1 = {"name": "Alice", "email": "alice@test.com"}
        response = await client.post(f"/tournaments/{tournament_id}/register", json=player1)
        assert response.status_code == 200



