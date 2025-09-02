from fastapi import FastAPI
from app.api import auth, users, restaurants, votes
from app.database import Base, engine
from app.api import leaderboard

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Restaurant Voting System")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(restaurants.router, prefix="/restaurants", tags=["restaurants"])
app.include_router(votes.router, prefix="/votes", tags=["votes"])
app.include_router(leaderboard.router, prefix="/leaderboard", tags=["leaderboard"])


# DATABASE_URL = postgresql://postgres:%40Darshik123@localhost:5432/restaurant

# SECRET_KEY = weresfsdfdgbvb56h5h5thgfhgj
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 60
