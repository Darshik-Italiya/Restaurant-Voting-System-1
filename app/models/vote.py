from sqlalchemy import Column, Integer, Float, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, date
from app.database import Base


class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    points = Column(Float, default=1.0)
    vote_date = Column(Date, default=date.today)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="votes")
    restaurant = relationship("Restaurant", back_populates="votes")
