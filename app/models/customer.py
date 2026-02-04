import uuid
from sqlalchemy import Column, String, Integer, Numeric, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    business_id = Column(UUID(as_uuid=True), ForeignKey("businesses.id"), nullable=False)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    notes = Column(Text, nullable=True)
    total_spent = Column(Numeric(10, 2), default=0)
    visit_count = Column(Integer, default=0)
    last_visit_at = Column(DateTime, nullable=True)

    # Relationships
    business = relationship("Business", back_populates="customers")
    visits = relationship("Visit", back_populates="customer")
    bookings = relationship("Booking", back_populates="customer")
