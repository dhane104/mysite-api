from typing import List
from typing import Union
import json
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal,engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
  
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#depedency
def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

#decorater
@app.post("/user",response_model=schemas.User)
def create_user(user: schemas.UserCreate, db:Session=Depends(get_db)):
    db_user =crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="email already resistered")
    return crud.create_user(db=db, user=user)  

@app.get("/users/",response_model=List[schemas.User])
def read_users(skip: int=0, limit: int =100,db:Session =Depends (get_db)):
    users =crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/user/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/user/{user_id}/posts/", response_model=schemas.Post)
def create_post_for_user(
    user_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)
):
    return crud.create_user_post(db=db, post=post, user_id=user_id)


@app.get("/api/v1/post/all")
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return {
        "message":"Data retrived sucessfully",
        "status":"sucess",
        "data": posts
    }

@app.get("/")
def read_root():
    return {"Hello": "World"}



# @app.get("/api/v1/post/all")
# def read_all_posts():
#     f = open('./data/posts.json')
#     data = json.load(f)

    


#     # return{
#     #     message: "Read Successfully",
#     #     status: "success",
#     #     data: data
#     # }
#     return data;
