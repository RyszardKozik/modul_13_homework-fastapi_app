import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import engine
from .models import Base
from .routers import auth, users, contacts
from .routers.users import router as users_router
from .routers.contacts import router as contacts_router
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Initialize FastAPI application
app = FastAPI()

# Middleware configuration for CORS (Cross-Origin Resource Sharing)
# This allows the API to be accessed from different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables in the database if they don't exist
Base.metadata.create_all(bind=engine)

# Include routers for different endpoints
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(contacts.router, prefix="/contacts", tags=["contacts"])

@app.get("/")
def read_root():
    """
    Root endpoint.

    Returns:
        dict: A greeting message.
    """
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
