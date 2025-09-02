from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, Token, UserOut
from app.crud import user as crud_user
from app.database import get_db
from app.core.security import verify_password, create_access_token

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if crud_user.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_user.create_user(db, user.username, user.email, user.password)


@router.post("/login", response_model=Token)
def login(form_data: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, form_data.email)
    if not db_user or not verify_password(form_data.password, str(db_user.hashed_password)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    token = create_access_token({"user_id": db_user.id})
    return {"access_token": token, "token_type": "bearer"}
