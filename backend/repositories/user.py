
from typing import List, Optional, Union

from models.dto.user import SignUpRequest
from models.user import UserModel
from repositories.schemas.user import User
from utils.password_handler import PasswordHandler

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from config import config

class UserRepository:
    """
    Store user's database
    """

    def __init__(self):
        self._engine = create_engine(config['DATABASE_URL'])
        self._DBSession = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self._engine))

    def findOne(self, email: str) -> Optional[UserModel]:
        result = self._DBSession.query(User).where(User.email == 'email').first()
        print(result)
        return result != None
    
    def create(self, user: SignUpRequest) -> Exception:
        assert user.email and user.name and user.password , "Email, name and password must not be null!"
        assert not self.findOne(user.email), "Email used before!"

        try:
            new_user = User(**user.model_dump())
            self._DBSession.add(new_user)
            self._DBSession.commit()

            return None
        except:
            print('Adding user failed! Rolled back')
            self._DBSession.rollback()

            return Exception('Cannot add user!')

