from pydantic import BaseModel
from datetime import date


class VoteCreate(BaseModel):
    restaurant_id: int


class VoteOut(BaseModel):
    id: int
    user_id: int
    restaurant_id: int
    points: float
    vote_date: date

    class Config:
        from_attributes = True
