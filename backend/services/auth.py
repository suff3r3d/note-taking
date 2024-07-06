from fastapi import Depends
from models.dto.user import SignUpRequest, SignUpResponse
from repositories.user import UserRepository

class AuthService:
    def __init__(self, repo: UserRepository = Depends(UserRepository)):
        self._repo = repo
        
    def signup(self, signup_info: SignUpRequest):
        # Should implement validations here

        print('Creating ', signup_info)

        signup_result = self._repo.create(signup_info)
        if signup_result == None:
            return SignUpResponse(success=True, message=None)
        else:
            return SignUpResponse(success=False, message=str(signup_result))
    
    