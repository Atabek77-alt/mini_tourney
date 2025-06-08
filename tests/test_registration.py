from fastapi.testclient import TestClient
from app.main import app
from app.db import Base, engine
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True)
async def tournaments_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

def test_full_flow():

    tournament_data = {
        "name": "Test Cup",
        "max_players": 2,
        "start_at": "2024-01-01T12:00:00"
    }
    response = client.post("/tournaments", json=tournament_data)
    assert response.status_code == 200
    tournament_id = response.json()["id"]


    player1 = {"name": "Alice", "email": "alice@test.com"}
    response = client.post(f"/tournaments/{tournament_id}/register", json=player1)
    assert response.status_code == 200


    player2 = {"name": "Bob", "email": "bob@test.com"}
    response = client.post(f"/tournaments/{tournament_id}/register", json=player2)
    assert response.status_code == 200


    player3 = {"name": "Eve", "email": "eve@test.com"}
    response = client.post(f"/tournaments/{tournament_id}/register", json=player3)
    assert response.status_code == 400
    assert "Tournament is full" in response.text

