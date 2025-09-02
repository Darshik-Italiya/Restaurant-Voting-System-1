from pydantic import BaseModel


class VoteCreate(BaseModel):
    restaurant_id: int
