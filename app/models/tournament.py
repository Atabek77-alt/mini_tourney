from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base


class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    max_players = Column(Integer)
    start_at = Column(DateTime)

    players = relationship("Player", back_populates="tournament")

    # @property
    # def registered_players(self) -> int:
    #     return len(self.players)


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))

    tournament = relationship("Tournament", back_populates="players")
