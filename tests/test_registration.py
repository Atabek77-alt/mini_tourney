# tests/test_registration.py
import pytest
from httpx import AsyncClient
from fastapi import FastAPI

# Создаем тестовое приложение
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@pytest.mark.asyncio
async def test_basic_flow():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Тест доступности сервера
        response = await client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}

