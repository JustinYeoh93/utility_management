from sqlalchemy import String, Column
from database import Base


class Utility(Base):
    __tablename__ = 'utilities'

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)

    checkout = relationship('Checkout', back_populates='utility')

    # Many to many
    user = relationship('User', secondary=admin_table, back_populates='utility')
