from datetime import datetime
from typing import Optional
from uuid import UUID
from decimal import Decimal
from pydantic import BaseModel


class CustomerCreate(BaseModel):
    name: str
    phone: str
    notes: Optional[str] = None


class CustomerResponse(BaseModel):
    id: UUID
    business_id: UUID
    name: str
    phone: str
    notes: Optional[str] = None
    total_spent: Decimal
    visit_count: int
    last_visit_at: Optional[datetime] = None

    class Config:
        from_attributes = True
