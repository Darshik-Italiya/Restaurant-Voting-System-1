from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date, timedelta
from app.database import get_db
from app.models.vote import Vote
from app.models.restaurant import Restaurant

router = APIRouter()


def calculate_leaderboard(db: Session, start_date: date, end_date: date):
    # total points per restaurant
    results = (
        db.query(Vote.restaurant_id, func.sum(Vote.points).label("total_points"))
        .filter(Vote.vote_date >= start_date, Vote.vote_date <= end_date)
        .group_by(Vote.restaurant_id)
        .order_by(func.sum(Vote.points).desc())
        .all()
    )

    leaderboard = []
    for r_id, points in results:
        restaurant = db.query(Restaurant).filter(Restaurant.id == r_id).first()
        if restaurant:
            leaderboard.append({"restaurant": restaurant.name, "points": points})
    return leaderboard


@router.get("/daily")
def daily_leaderboard(db: Session = Depends(get_db)):
    today = date.today()
    return calculate_leaderboard(db, today, today)


@router.get("/weekly")
def weekly_leaderboard(db: Session = Depends(get_db)):
    today = date.today()
    start = today - timedelta(days=today.weekday())  # Monday
    return calculate_leaderboard(db, start, today)


@router.get("/monthly")
def monthly_leaderboard(db: Session = Depends(get_db)):
    today = date.today()
    start = today.replace(day=1)
    return calculate_leaderboard(db, start, today)
