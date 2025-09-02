from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.db.database import engine
from app.db.base import Base

# Import routers
# from app.routers import auth, users, estimates

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Estimation Platform API"
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
# app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
# app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
# app.include_router(estimates.router, prefix="/api/v1/estimates", tags=["estimates"])

@app.get("/")
async def root():
    return {"message": "Welcome to Estimation Platform API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
