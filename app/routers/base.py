from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    """Welcome endpoint for the API"""
    return {"message": "Welcome to Estimation Platform API"}


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@router.get("/ping")
async def ping():
    """Simple ping endpoint for testing"""
    return {"message": "pong"}


@router.get("/version")
async def version():
    """API version endpoint"""
    return {
        "version": "1.0.0",
        "service": "Estimation Platform",
        "status": "running"
    }
