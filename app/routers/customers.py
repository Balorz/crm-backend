from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_business
from app.models.business import Business
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerResponse

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("", response_model=CustomerResponse)
def create_customer(
    customer_data: CustomerCreate,
    db: Session = Depends(get_db),
    business: Business = Depends(get_current_business)
):
    """Create a new customer for the business."""
    customer = Customer(
        business_id=business.id,
        name=customer_data.name,
        phone=customer_data.phone,
        notes=customer_data.notes
    )
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


@router.get("", response_model=List[CustomerResponse])
def list_customers(
    db: Session = Depends(get_db),
    business: Business = Depends(get_current_business)
):
    """List all customers for the current business."""
    return db.query(Customer).filter(Customer.business_id == business.id).all()
