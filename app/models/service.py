import uuid
from sqlalchemy import Column, String, Integer, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base


class Service(Base):
    __tablename__ = "services"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    business_id = Column(UUID(as_uuid=True), ForeignKey("businesses.id"), nullable=False)
    name = Column(String, nullable=False)
    default_duration_min = Column(Integer, nullable=False)
    default_price = Column(Numeric(10, 2), nullable=True)

    # Relationships
    business = relationship("Business", back_populates="services")
    visits = relationship("Visit", back_populates="service")
    bookings = relationship("Booking", back_populates="service")
