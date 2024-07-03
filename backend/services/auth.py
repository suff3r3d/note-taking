from fastapi import Depends
from models.dto.user import SignUpRequest, SignUpResponse
from repositories.user import UserRepository

class AuthService:
    def __init__(self, repo: UserRepository = Depends(UserRepository)):
        self._repo = repo
        
    def signup(self, signup_info: SignUpRequest):
        if (self._repo.findOne(signup_info.email)):
            return SignUpResponse(success=False, message="Email used!")

        # Should implement validations here
        
        self._repo.create(signup_info)
        return SignUpResponse(success=True, message=None)
    
    