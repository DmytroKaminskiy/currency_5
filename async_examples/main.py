import models
import schemas
from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List


app = FastAPI()


# create
models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def index_get():
    return {"message": "Hello World GET"}


@app.post("/")
async def index_post():
    return {"message": "Hello World POST"}


@app.get('/profiles')
async def profiles_get(
        db: Session = Depends(get_db),
        response_model=List[schemas.User],
):
    users = db.query(models.User).all()
    return users


# @app.get('/profiles/{profile_id}')
# async def profiles_get(profile_id: int):
#     return PROFILES.get(profile_id) or {}
