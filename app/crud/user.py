from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password


def create_user(db: Session, username: str, email: str, password: str):
    db_user = User(
        username=username, email=email, hashed_password=hash_password(password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
