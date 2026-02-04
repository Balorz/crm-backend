from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_business
from app.models.business import Business
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceResponse

router = APIRouter(prefix="/services", tags=["Services"])


@router.post("", response_model=ServiceResponse)
def create_service(
    service_data: ServiceCreate,
    db: Session = Depends(get_db),
    business: Business = Depends(get_current_business)
):
    """Add a new service to the business."""
    service = Service(
        business_id=business.id,
        name=service_data.name,
        default_duration_min=service_data.default_duration_min,
        default_price=service_data.default_price
    )
    db.add(service)
    db.commit()
    db.refresh(service)
    return service


@router.get("", response_model=List[ServiceResponse])
def list_services(
    db: Session = Depends(get_db),
    business: Business = Depends(get_current_business)
):
    """List all services for the current business."""
    return db.query(Service).filter(Service.business_id == business.id).all()
