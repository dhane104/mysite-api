from sqlalchemy.orm import Session 
import models,schemas
def get_user(db:Session,user_id:int):
    return db.query(models.User).filter(models.User.id==user_id).first()
def get_user_by_email(db:Session,email:str):
    return db.query(models.User).filter(models.User.email==email).first()
def get_users(db:Session,skip:int=0,limit:int=100):
    return db.query(models.User).offset(skip).limit(limit).all()
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def create_user_post(db: Session, post: schemas.PostCreate, user_id: int):
    db_post = models.Post(**post.dict(), user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db:Session,skip:int=0,limit:int=100):
    return db.query(models.Post).offset(skip).limit(limit).all()
