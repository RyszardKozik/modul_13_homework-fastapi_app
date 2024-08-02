from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    """
    Base model for User schema.
    """
    username: str
    email: str

class UserCreate(UserBase):
    """
    Schema for creating a new user.
    """
    password: str

class UserUpdate(UserBase):
    """
    Schema for updating user information.
    """
    password: Optional[str] = None

class UserOut(UserBase):
    """
    Schema for outputting user information.
    """
    id: int

    class Config:
        orm_mode = True

class PhotoBase(BaseModel):
    """
    Base model for Photo schema.
    """
    title: str
    description: Optional[str] = None

class PhotoCreate(PhotoBase):
    """
    Schema for creating a new photo.
    """
    image_url: str

class PhotoOut(PhotoBase):
    """
    Schema for outputting photo information.
    """
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    """
    Base model for Comment schema.
    """
    content: str

class CommentCreate(CommentBase):
    """
    Schema for creating a new comment.
    """
    pass

class CommentOut(CommentBase):
    """
    Schema for outputting comment information.
    """
    id: int
    user_id: int
    photo_id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """
    Schema for token data.
    """
    username: Optional[str] = None
