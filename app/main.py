from fastapi import FastAPI
from app.api import auth, users, restaurants, votes
from app.database import Base, engine
from app.api import leaderboard
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Restaurant Voting System")

origins = ["http://localhost:5174"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Users"])
# app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(restaurants.router, prefix="/restaurants", tags=["Restaurants"])
app.include_router(votes.router, prefix="/votes", tags=["Votes"])
app.include_router(leaderboard.router, prefix="/leaderboard", tags=["Leaderboard"])
