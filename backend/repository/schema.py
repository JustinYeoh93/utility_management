from sqlalchemy import String, Column, Enum, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

import enum

Base = declarative_base()


class Utility(Base):
    __tablename__ = "utilities"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)

    checkout = relationship("Checkout", back_populates="utility")

    # Many to many
    user = relationship("User", secondary="admins", back_populates="utility")


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    checkout = relationship("Checkout", back_populates="user")

    # Many to many
    utility = relationship("Utility", secondary="admins", back_populates="user")


class StatusEnum(enum.Enum):
    checked_out = "checked_out"
    returned = "returned"


class Checkout(Base):
    __tablename__ = "checkouts"

    id = Column(String, primary_key=True, index=True)
    status = Column(Enum(StatusEnum), nullable=False)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    utilitiy_id = Column(String, ForeignKey("utilities.id"), nullable=False)

    user = relationship("User", back_populates="checkout")
    utility = relationship("Utility", back_populates="checkout")


class Admin(Base):
    __tablename__ = "admins"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))
    utility_id = Column(String, ForeignKey("utilities.id"))

    __table_args__ = (
        UniqueConstraint("user_id", "utility_id", name="_user_utility_uc"),
    )
