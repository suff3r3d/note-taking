#using bcrypt for simplicity

import bcrypt

class PasswordHandler:
    @staticmethod
    def hash(password: bytes) -> bytes:
        return bcrypt.hashpw(password, bcrypt.gensalt())
    
    @staticmethod
    def verify(password: bytes, hashed: bytes) -> bool:
        return bcrypt.checkpw(password, hashed)