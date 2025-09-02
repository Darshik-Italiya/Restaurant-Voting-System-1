from sqlalchemy.orm import Session
from datetime import date
from app.models.vote import Vote


def get_votes_today(db: Session, user_id: int):
    today = date.today()
    return (
        db.query(Vote)
        .filter(Vote.user_id == user_id, Vote.vote_date == today)
        .all()
    )


def create_vote(db: Session, user_id: int, restaurant_id: int, points: float):
    vote = Vote(user_id=user_id, restaurant_id=restaurant_id, points=points)
    db.add(vote)
    db.commit()
    db.refresh(vote)
    return vote
