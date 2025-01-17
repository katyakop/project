from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, User, UserCreate


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/")
def user(db: Session = Depends(get_db)):
    return db.query(User).all()
