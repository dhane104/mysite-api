from sqlalchemy import Boolean,Column,ForeignKey,Integer,String
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON

from database import Base


class User(Base):
     __tablename__="users"
     id  = Column(Integer, primary_key=True, index=True)
     email = Column(String(length=50), unique=True, index=True)
     password = Column(String(length=50))
     is_active = Column(Boolean, default=True)
     posts = relationship("Post",back_populates="user")

class Post(Base):
    __tablename__="posts"

    id =Column(Integer,primary_key=True, index=True)
    title =Column(String(length=50), index=True) 
    location= Column(String(length=50))
    user_id = Column(Integer, ForeignKey("users.id"))
    userprofile=Column(String(length=50))
    post_by=Column(String(length=50))
    post=Column(String(length=50))
    is_full_time=Column(String(length=50), index=True)
    active=Column(String(length=50))
    option1=Column(String(length=50))
    option2=Column(String(length=50))
    option3=Column(String(length=50))
    option4=Column(String(length=50))
    option5=Column(String(length=50))
    pay_rate=Column(Integer)
    skills=Column(JSON(String(length=50)))
    like_count=Column(Integer)
    comments=Column(JSON(String(length=50)))
    description=Column(String(length=50), index=True) 
    comnt=Column(Integer)
    views=Column(Integer)
    post_datetime=Column(Integer)



    user = relationship("User",back_populates="posts")