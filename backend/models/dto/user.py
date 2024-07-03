from pydantic import BaseModel

class SignInRequest(BaseModel):
    email: str
    password: str

class SignUpRequest(BaseModel):
    name: str
    email: str
    password: str

class SignUpResponse(BaseModel):
    success: bool
    message: str | None