
from typing import List, Optional

from models.dto.user import SignUpRequest
from models.user import UserModel
from utils.password_handler import PasswordHandler


class UserRepository:
    """
    Store user's database
    """

    def __init__(self):
        self._repo: List[UserModel] = []

    def findOne(self, email: str) -> Optional[UserModel]:
        for user in self._repo:
            if user.email == email:
                return user
            
        return None
    
    def create(self, user: SignUpRequest):
        assert user.email and user.name and user.password , "Email, name and password must not be null!"
        assert not self.findOne(user.email), "Email used before!"

        self._repo.append(UserModel(name = user.name, email = user.email, hashedPassword = PasswordHandler.hash(user.password)))

