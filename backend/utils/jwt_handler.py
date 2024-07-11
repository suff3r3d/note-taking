from base64 import urlsafe_b64decode, urlsafe_b64encode
from json import dumps, loads
import hmac
from hashlib import sha256
from typing import Optional, Tuple
from config import config

class Base64:
    @staticmethod
    def encode(data: str) -> str:
        return urlsafe_b64encode(data.encode()).decode().rstrip('=')
    
    @staticmethod
    def decode(data: str) -> str:
        enc = data + '=' * (-len(data) % 4)
        return urlsafe_b64decode(enc.encode()).decode()

class JWTHandler:
    '''
    Currently, there's no expiration since I haven't learned Redis

    In practice, each jwt have its' own secret which is stored in Redis. Right now, I am using the same for
    '''

    @staticmethod
    def create(payload: dict) -> str:
        try:
            secret = 'secret'
            assert(secret != None)

            '''
            Expiration date of the token (Redis)
            '''

            token =  ".".join([
                Base64.encode(dumps({"alg": "HS256", "typ": "JWT"})),
                Base64.encode(dumps(payload)),
                JWTHandler.sign(payload, secret)
            ])
            
            print(token)
            print(JWTHandler.verify(token))

            return token
        except Exception as e:
            return str(e)
    
    @staticmethod
    def verify(data: str) -> Tuple[Optional[dict], Exception]:
        # Notice the expiration part, too
        try:
            _, payload, signature = data.split('.')

            '''
            Expiration date here (Redis)
            Might add a new UserModel's properties (uuid)
            '''

            payload = loads(Base64.decode(payload))
            secret = 'secret'
            assert signature == JWTHandler.sign(payload, secret)

            return [payload, None]
        except Exception as e:
            return [None, e]
            
    
    @staticmethod
    def sign(payload: dict, secret: str) -> str:
        payload = Base64.encode(dumps({"alg": "HS256", "typ": "JWT"})) + '.' + Base64.encode(dumps(payload))
        return Base64.encode(hmac.new(secret.encode(), payload.encode(), sha256).hexdigest())
    
    
