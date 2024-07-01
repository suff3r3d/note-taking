#using bcrypt for simplicity

import bcrypt

class PasswordHandler:
    @staticmethod
    def hash(password: str) -> bytes:
        return bytes.decode(bcrypt.hashpw(password.encode(), bcrypt.gensalt()), "utf-8")
    
    @staticmethod
    def verify(password: str, hashed: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed.encode())