from repositories.schemas import Base
from sqlalchemy import Column, String

class User(Base):
    # used to interact with database
    __tablename__ = 'users'

    name = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index = True)
    email = Column(String, unique=True, index=True)
    hashedpassword = Column(String)