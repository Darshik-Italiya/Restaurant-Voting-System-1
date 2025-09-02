from sqlalchemy.orm import Session
from app.models.restaurant import Restaurant


def create_restaurant(db: Session, name: str, description: str, creator_id: int):
    restaurant = Restaurant(name=name, description=description, creator_id=creator_id)
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant


def list_restaurants(db: Session):
    return db.query(Restaurant).all()
