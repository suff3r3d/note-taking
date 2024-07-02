from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.dto.user import SignInRequest, SignUpRequest
from models.user import UserModel
from repositories.user import UserRepository
from utils.password_handler import PasswordHandler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://127.0.0.1:5173'
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

repo = UserRepository()
repo.create(SignUpRequest(name = "Chung Dinh", email = "hgchung.dinh@gmail.com", password = '123'))

@app.get("/hash/{password}")
def get_hashed(password: str):
    return {"hash": PasswordHandler.hash(password)}

@app.get("/user/{email}")
def find_user(email: str):
    return {"response": repo.findOne(email)}

@app.post("/api/signup")
def signup():
    pass