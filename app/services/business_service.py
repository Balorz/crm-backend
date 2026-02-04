from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.business import Business
from app.models.user import User
from app.schemas.business import BusinessCreate


def create_business(db: Session, business_data: BusinessCreate, user: User) -> Business:
    # Check if user already has a business
    existing_business = db.query(Business).filter(Business.user_id == user.id).first()
    if existing_business:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already has a business. Only one business per user allowed in Phase 1."
        )
    
    # Create new business
    business = Business(
        user_id=user.id,
        name=business_data.name,
        business_type=business_data.business_type,
        address=business_data.address,
        working_hours=business_data.working_hours
    )
    db.add(business)
    db.commit()
    db.refresh(business)
    return business


def get_user_business(db: Session, user: User) -> Business:
    business = db.query(Business).filter(Business.user_id == user.id).first()
    if not business:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Business not found"
        )
    return business
