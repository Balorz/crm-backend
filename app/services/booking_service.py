from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.booking import Booking
from app.models.customer import Customer
from app.models.service import Service
from app.models.business import Business
from app.schemas.booking import BookingCreate


def create_booking(db: Session, booking_data: BookingCreate, business: Business) -> Booking:
    # Verify customer belongs to this business
    customer = db.query(Customer).filter(
        Customer.id == booking_data.customer_id,
        Customer.business_id == business.id
    ).first()
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    
    # Verify service belongs to this business
    service = db.query(Service).filter(
        Service.id == booking_data.service_id,
        Service.business_id == business.id
    ).first()
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found"
        )
    
    # Calculate end_time based on service duration
    end_time = booking_data.start_time + timedelta(minutes=service.default_duration_min)
    
    # Create booking
    booking = Booking(
        business_id=business.id,
        customer_id=booking_data.customer_id,
        service_id=booking_data.service_id,
        start_time=booking_data.start_time,
        end_time=end_time,
        status="booked"
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking
