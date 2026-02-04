from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.visit import Visit
from app.models.customer import Customer
from app.models.service import Service
from app.models.business import Business
from app.schemas.visit import VisitCreate


def create_visit(db: Session, visit_data: VisitCreate, business: Business) -> Visit:
    # Verify customer belongs to this business
    customer = db.query(Customer).filter(
        Customer.id == visit_data.customer_id,
        Customer.business_id == business.id
    ).first()
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    
    # Verify service belongs to this business
    service = db.query(Service).filter(
        Service.id == visit_data.service_id,
        Service.business_id == business.id
    ).first()
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found"
        )
    
    # Create visit
    visit = Visit(
        business_id=business.id,
        customer_id=visit_data.customer_id,
        service_id=visit_data.service_id,
        amount_paid=visit_data.amount_paid
    )
    db.add(visit)
    
    # Update customer stats
    customer.visit_count += 1
    customer.total_spent += visit_data.amount_paid
    customer.last_visit_at = datetime.utcnow()
    
    db.commit()
    db.refresh(visit)
    return visit
