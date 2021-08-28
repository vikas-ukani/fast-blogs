import jwt
from decouple import config
import time
from typing import Dict

JWT_SECRET = config('secret')
JWT_ALGORITHM = config('algorithm')


def token_response(token: str):
    return {
        'token': token
    }


def signJWT(userId: str) -> Dict[str, str]:
    payload = {
        "user_Id": userId,
        'expires': time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    print('token', token)
    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        print(decoded_token)

        if decoded_token['expires'] >= time.time():
            return decoded_token
        else:
            return None
    except:
        return {}
