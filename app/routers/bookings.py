from datetime import datetime, date
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_business
from app.models.business import Business
from app.models.booking import Booking
from app.schemas.booking import BookingCreate, BookingResponse
from app.services.booking_service import create_booking

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.post("", response_model=BookingResponse)
def create_new_booking(
    booking_data: BookingCreate,
    db: Session = Depends(get_db),
    business: Business = Depends(get_current_business)
):
    """Create a new booking. End time is auto-calculated from service duration."""
    return create_booking(db, booking_data, business)


@router.get("/today", response_model=List[BookingResponse])
def get_today_bookings(
    db: Session = Depends(get_db),
    business: Business = Depends(get_current_business)
):
    """Get all bookings for today."""
    today = date.today()
    today_start = datetime.combine(today, datetime.min.time())
    today_end = datetime.combine(today, datetime.max.time())
    
    return db.query(Booking).filter(
        Booking.business_id == business.id,
        Booking.start_time >= today_start,
        Booking.start_time <= today_end
    ).order_by(Booking.start_time).all()
