
from typing import List, Optional, Union

from models.dto.user import SignUpRequest
from models.user import UserModel
from repositories.schemas.user import User
from utils.password_handler import PasswordHandler

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from config import config as cfg

import bcrypt

class UserRepository:
    """
    Store user's database
    """

    def __init__(self):
        self._engine = create_engine(cfg['DATABASE_URL'])
        self._DBSession = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self._engine))

    def findEmail(self, email: str) -> bool:
        result = self._DBSession.query(User).where(User.email == email).first()
        return result != None

    def findUsername(self, username: str) -> bool:
        result = self._DBSession.query(User).where(User.username == username).first()
        return result != None
    
    def create(self, user: SignUpRequest) -> Exception:
        try:
            assert user.email and user.username and user.name and user.password , "Email, name, username and password must not be null!"
            assert not self.findEmail(user.email), "Email used!"
            assert not self.findUsername(user.username), "Username used!"

            new_user = User()

            new_user.username = user.username
            new_user.name = user.name
            new_user.email = user.email
            new_user.hashedpassword = bcrypt.hashpw(user.password.encode(), cfg['BCRYPT_SECRET'])

            self._DBSession.add(new_user)
            self._DBSession.commit()

            return None
        except Exception as e:
            print('Adding user failed! Rolled back')
            self._DBSession.rollback()

            return e

