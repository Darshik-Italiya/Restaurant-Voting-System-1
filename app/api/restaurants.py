from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.restaurant import RestaurantCreate, RestaurantOut
from app.crud import restaurant as crud_restaurant
from app.database import get_db
from app.dependencies import get_current_user
from app.models.restaurant import Restaurant

router = APIRouter()


@router.post("/", response_model=RestaurantOut)
def create_restaurant(
    data: RestaurantCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return crud_restaurant.create_restaurant(db, data.name, data.description, user.id)


@router.get("/", response_model=list[RestaurantOut])
def list_restaurants(db: Session = Depends(get_db)):
    return crud_restaurant.list_restaurants(db)


@router.delete("/{restaurant_id}")
def delete_restaurant(
    restaurant_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)
):
    restaurant = db.query(Restaurant).filter_by(id=restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    if restaurant.creator_id != user.id:
        raise HTTPException(
            status_code=403, detail="You can only delete your own restaurants"
        )
    db.delete(restaurant)
    db.commit()
    return {"detail": "Restaurant deleted successfully"}
