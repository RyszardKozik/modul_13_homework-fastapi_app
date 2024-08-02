from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.schemas import Token
from app import schemas, crud, models
from app.dependencies import get_db
from app.auth_utils import create_access_token, get_password_hash
from app.email_utils import send_reset_password_email
from app.config import settings

# Define the API router
router = APIRouter()

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Define the OAuth2 password bearer scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.post("/login", response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Endpoint to log in a user.

    Args:
        form_data (OAuth2PasswordRequestForm): The form data containing username and password.
        db (Session): Database session dependency.

    Returns:
        dict: JWT access and refresh tokens.
    """
    user = crud.authenticate_user(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/refresh", response_model=schemas.Token)
async def refresh_token(token: str, db: Session = Depends(get_db)):
    """
    Endpoint to refresh the JWT token.

    Args:
        token (str): The current JWT token.
        db (Session): Database session dependency.

    Returns:
        dict: New JWT access token.
    """
    # Implement refresh token logic here...
    pass

@router.post("/reset-password")
async def reset_password(email: str, db: Session = Depends(get_db)):
    """
    Endpoint to initiate the password reset process.

    Args:
        email (str): The user's email.
        db (Session): Database session dependency.

    Returns:
        dict: A success message.
    """
    # Implement password reset logic here...
    pass
