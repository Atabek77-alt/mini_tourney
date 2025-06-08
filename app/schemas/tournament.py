from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import List

class TournamentCreate(BaseModel):
    name: str
    max_players: int
    start_at: datetime





class PlayerRegister(BaseModel):
    name: str
    email: EmailStr


class PlayerRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


class TournamentRead(BaseModel):
    id: int
    name: str
    max_players: int
    start_at: datetime
    registered_players: List[PlayerRead] = []

    model_config = ConfigDict(from_attributes=True)