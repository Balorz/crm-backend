import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base


class Business(Base):
    __tablename__ = "businesses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)
    name = Column(String, nullable=False)
    business_type = Column(String, nullable=False)
    address = Column(String, nullable=True)
    working_hours = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="business")
    services = relationship("Service", back_populates="business")
    customers = relationship("Customer", back_populates="business")
    visits = relationship("Visit", back_populates="business")
    bookings = relationship("Booking", back_populates="business")
