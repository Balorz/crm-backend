import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, business, services, customers, visits, bookings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="AI Adaptive CRM",
    description="Phase 1 Backend - Foundation APIs for Mini CRM",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(business.router)
app.include_router(services.router)
app.include_router(customers.router)
app.include_router(visits.router)
app.include_router(bookings.router)


@app.get("/", tags=["Health"])
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "version": "1.0.0"}


@app.on_event("startup")
async def startup_event():
    logger.info("AI Adaptive CRM Backend starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("AI Adaptive CRM Backend shutting down...")
