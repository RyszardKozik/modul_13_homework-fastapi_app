from sqlalchemy.orm import Session
from app import models, schemas

# Function to get user by email
def get_user_by_email(db: Session, email: str) -> models.User:
    return db.query(models.User).filter(models.User.email == email).first()

# Function to create a new user
def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(email=user.email, hashed_password=user.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Function to update user details
def update_user(db: Session, user: models.User, update_data: dict) -> models.User:
    for key, value in update_data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

# Function to delete a user
def delete_user(db: Session, user: models.User) -> None:
    db.delete(user)
    db.commit()
