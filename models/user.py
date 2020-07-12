from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.admin import admin_table

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    department = Column(String)
    email = Column(String, unique=True)

    checkout = relationship('Checkout', back_populates='user')

    # Many to many
    utility = relationship('Utility', secondary=admin_table, back_populates='user')
