from sqlalchemy import Column, String, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    user_name = Column(String)
    password = Column(String)
    email = Column(String)

    admin_rooms = relationship("Room", back_populates="room_admin")
    rooms = relationship("Member", back_populates="room_members")


class Room(Base):
    __tablename__ = "rooms"
    id = Column(String, primary_key=True)
    room_name = Column(String)
    admin_id = Column(String, ForeignKey("users.id"))

    room_admin = relationship("User", back_populates="admin_rooms")
    members = relationship("Member", back_populates="member_rooms")
    items = relationship("Item", back_populates="room")


class Item(Base):
    __tablename__ = "items"
    item_name = Column(String, primary_key=True)
    quantity = Column(Float(precision=2))
    room_id = Column(String, ForeignKey("rooms.id"))

    room = relationship("Room", back_populates="items")


class Member(Base):
    __tablename__ = "members"
    user_id = Column(String, ForeignKey("users.id"), primary_key=True)
    room_id = Column(String, ForeignKey("rooms.id"), primary_key=True)

    member_rooms = relationship("Room", back_populates="members")
    room_members = relationship("User", back_populates="rooms")

