from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class BookingCreate(BaseModel):
    customer_id: UUID
    service_id: UUID
    start_time: datetime


class BookingResponse(BaseModel):
    id: UUID
    business_id: UUID
    customer_id: UUID
    service_id: UUID
    start_time: datetime
    end_time: datetime
    status: str

    class Config:
        from_attributes = True


class BookingUpdate(BaseModel):
    status: Optional[str] = None
