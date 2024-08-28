from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.dto.user import SignInRequest, SignUpRequest, SignUpResponse
from models.user import UserModel
from repositories.user import UserRepository
from services.auth import AuthService
from utils.password_handler import PasswordHandler
from utils.jwt_handler import JWTHandler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:5173'
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



'''
@app.get("/hash/{password}")
def get_hashed(password: str):
    return {"hash": PasswordHandler.hash(password)}

@app.get("/user/{email}")
def find_user(email: str):  Ư2  ` 0+

    return {"response": repo.findOne(email)}
'''

@app.post("/api/signup")
def signup(signup_info: SignUpRequest, auth_service: AuthService = Depends(AuthService)):
    #print(signup_info)
    res: SignUpResponse = auth_service.signup(signup_info)
    return res

@app.post("/create_jwt/{data}")
def create_jwt(data: str):
    return JWTHandler.create({"data": data})