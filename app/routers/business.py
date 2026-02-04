from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.models.user import User
from app.schemas.business import BusinessCreate, BusinessResponse
from app.services.business_service import create_business, get_user_business

router = APIRouter(prefix="/business", tags=["Business"])


@router.post("", response_model=BusinessResponse)
def create_new_business(
    business_data: BusinessCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a business for the logged-in user."""
    return create_business(db, business_data, current_user)


@router.get("/me", response_model=BusinessResponse)
def get_my_business(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get the business info for the logged-in user."""
    return get_user_business(db, current_user)
