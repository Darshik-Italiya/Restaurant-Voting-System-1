from pydantic import BaseModel


class RestaurantCreate(BaseModel):
    name: str
    description: str | None = None


class RestaurantOut(BaseModel):
    id: int
    name: str
    description: str | None
    creator_id: int

    class Config:
        from_attributes = True
