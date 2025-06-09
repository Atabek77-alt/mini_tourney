# MiniTourney

Минималистичный сервис для создания турниров и регистрации участников на FastAPI и PostgreSQL (async).

---

## Структура проекта

- **app/** — исходный код приложения  
  - **main.py** — точка входа, инициализация FastAPI и роутеров  
  - **config.py** — настройки подключения к БД (через Pydantic и переменные окружения)  
  - **database.py** — конфигурация SQLAlchemy AsyncSession и движка  
  - **models.py** — SQLAlchemy ORM модели (например, Participant)  
  - **schemas.py** — Pydantic модели для валидации запросов и ответов  
  - **routers/** — маршруты API, например регистрация участников на турниры  

- **.env** — переменные окружения для подключения к базе (DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

- **Dockerfile** и **docker-compose.yml** — для запуска приложения и базы в контейнерах

---

## Установка и запуск

1. Создайте `.env` с переменными подключения к PostgreSQL. Пример:
DB_USER=tournament_user
DB_PASSWORD=qwerty123
DB_HOST=db
DB_PORT=5432
DB_NAME=tournaments_db


2. Запустите PostgreSQL и приложение через Docker Compose (или вручную).

3. Запустите приложение командой:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
Использование API

POST /tournaments/{tournament_id}/register — регистрация участника на турнир
Тело запроса (JSON):
{
  "name": "Имя участника",
  "email": "email@example.com"
}
Ответ: объект участника с id, name, email.
Пример curl-запроса

curl -X POST "http://localhost:8000/tournaments/2/register" \
-H "Content-Type: application/json" \
-d '{"name": "Jhon", "email": "jhon@email.com"}'