from sqlalchemy import String, Column, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import enum


class StatusEnum(enum.Enum):
    checked_out = 'checked_out'
    returned = 'returned'


class Checkout(Base):
    __tablename__ = 'checkouts'

    id = Column(String, primary_key=True, index=True)
    status = Column(Enum(StatusEnum), nullable=False)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    utilitiy_id = Column(String, ForeignKey("utilities.id"), nullable=False)

    user = relationship('User', back_populates='checkout')
    utility = relationship('Utility', back_populates='checkout')
