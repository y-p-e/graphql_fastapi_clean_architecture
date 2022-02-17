from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from models import Base
from schemas import User
from database import SessionLocal, engine
from models import User as MUser

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/user/", response_model=User)
def read_users(user_name: str, db: Session = Depends(get_db)):
    user = db.query(MUser).filter(MUser.user_name == user_name).first()
    return user
