from datetime import datetime
from typing import Optional, Dict, Any
from uuid import UUID
from pydantic import BaseModel


class BusinessCreate(BaseModel):
    name: str
    business_type: str
    address: Optional[str] = None
    working_hours: Optional[Dict[str, Any]] = None


class BusinessResponse(BaseModel):
    id: UUID
    user_id: UUID
    name: str
    business_type: str
    address: Optional[str] = None
    working_hours: Optional[Dict[str, Any]] = None
    created_at: datetime

    class Config:
        from_attributes = True
