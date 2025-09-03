from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.vote import VoteCreate, VoteOut
from app.database import get_db
from app.dependencies import get_current_user
from app.models.vote import Vote
from app.crud.vote import get_votes_today, create_vote

router = APIRouter()

MAX_DAILY_VOTES = 3
POINTS_DECAY = [1, 0.5, 0.25]


@router.post("/", response_model=dict)
def vote(
    data: VoteCreate, db: Session = Depends(get_db), user=Depends(get_current_user)
):
    votes_today = get_votes_today(db, user.id)
    if len(votes_today) >= MAX_DAILY_VOTES:
        raise HTTPException(status_code=400, detail="Daily vote limit reached")

    # count votes on the same restaurant today
    same_restaurant_votes = len(
        [v for v in votes_today if getattr(v, "restaurant_id") == data.restaurant_id]
    )
    if same_restaurant_votes >= len(POINTS_DECAY):
        points = POINTS_DECAY[-1]
    else:
        points = POINTS_DECAY[same_restaurant_votes]

    vote = create_vote(db, user.id, data.restaurant_id, points)
    remaining_votes = MAX_DAILY_VOTES - len(votes_today) - 1
    return {"vote": vote.id, "points": points, "remaining_votes": remaining_votes}


@router.get("/my-votes", response_model=list[VoteOut])
def get_my_votes(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Vote).filter(Vote.user_id == user.id).all()
