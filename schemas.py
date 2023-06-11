from typing import List, Union

from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    description:Union[str,None]=None
    
    userprofile:str
    post_by:str
    post:str
    is_full_time:str
    active:str
    option1:str
    option2:str
    option3:str
    option4:str
    option5:str
    pay_rate:int
    skills:List[str]
    like_count:int
    comments:List[str]
    description:str 
    comnt:int
    views:int
    post_datetime:int


class PostCreate(PostBase):
    pass

class Post(PostBase):
    id:int
    user_id:int
    class Config:
        orm_mode=True

class UserBase(BaseModel):
    email:str

class UserCreate(UserBase):
    password:str


class User(UserBase):
    id:int
    is_active:bool
    Posts:List[Post]=[]

    class Config:
        orm_mode=True       

