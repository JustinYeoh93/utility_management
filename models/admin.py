from sqlalchemy import Column, String, ForeignKey, Table
from database import Base

admin_table = Table('admin', Base.metadata, Column('user_id', String, ForeignKey('users.id')),
                    Column('utility_id', String, ForeignKey('utilities.id')))
