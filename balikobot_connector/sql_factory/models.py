from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, CHAR
from sqlalchemy.orm import relationship
from .database import Base


class Shipment(Base):
    __tablename__ = 'shipments'

    id = Column(Integer, primary_key=True, index=True)
    original_id = Column(String,index=True)
    is_active = Column(Boolean, default=True)
    state = Column(CHAR, default='N')
    is_test = Column(Boolean, default=True)
