from datetime import datetime
from uuid import UUID
from decimal import Decimal
from pydantic import BaseModel


class VisitCreate(BaseModel):
    customer_id: UUID
    service_id: UUID
    amount_paid: Decimal


class VisitResponse(BaseModel):
    id: UUID
    business_id: UUID
    customer_id: UUID
    service_id: UUID
    visit_time: datetime
    amount_paid: Decimal

    class Config:
        from_attributes = True
