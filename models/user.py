from sqlalchemy import String, Column
from admin import admin_table

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
