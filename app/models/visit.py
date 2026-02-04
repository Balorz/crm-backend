import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base


class Visit(Base):
    __tablename__ = "visits"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    business_id = Column(UUID(as_uuid=True), ForeignKey("businesses.id"), nullable=False)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"), nullable=False)
    service_id = Column(UUID(as_uuid=True), ForeignKey("services.id"), nullable=False)
    visit_time = Column(DateTime, default=datetime.utcnow)
    amount_paid = Column(Numeric(10, 2), nullable=False)

    # Relationships
    business = relationship("Business", back_populates="visits")
    customer = relationship("Customer", back_populates="visits")
    service = relationship("Service", back_populates="visits")
