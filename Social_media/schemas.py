from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    email : EmailStr
    password : str
    

class UserOut(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime
    class Config:
        from_attributes = True
    
    
class UserLogin(BaseModel):
    email : EmailStr
    password : str
    

class Token(BaseModel):
    access_token : str
    token_type : str
    

class TokenData(BaseModel):
    id : Optional[int] = None
    
    
class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True
    

class CreatePost(PostBase):
    pass


class PostReponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    class Config:
        from_attributes = True


class PostOut(BaseModel):
    Post: PostReponse
    votes: int
    class Config:
        from_attributes = True
        

class Vote(BaseModel):
    post_id : int
    dir: int = Field(ge=0, le=1 ,description="Direction variable (0 or 1)", )
    