from pydantic import BaseModel, EmailStr
from datetime import datetime


class TournamentCreate(BaseModel):
    name: str
    max_players: int
    start_at: datetime


class TournamentRead(BaseModel):
    id: int
    name: str
    max_players: int
    start_at: datetime
    registered_players: int

    class Config:
        orm_mode = True


class PlayerRegister(BaseModel):
    name: str
    email: EmailStr


class PlayerRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
