from typing import Optional
from uuid import UUID
from decimal import Decimal
from pydantic import BaseModel


class ServiceCreate(BaseModel):
    name: str
    default_duration_min: int
    default_price: Optional[Decimal] = None


class ServiceResponse(BaseModel):
    id: UUID
    business_id: UUID
    name: str
    default_duration_min: int
    default_price: Optional[Decimal] = None

    class Config:
        from_attributes = True
