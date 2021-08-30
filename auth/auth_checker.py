from auth.auth_handler import decodeJWT
from fastapi.security import (
    HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordBearer)
from fastapi import Request, HTTPException


class AuthBearer(HTTPBearer):
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    def __init__(self, auto_error: bool = True):
        super(AuthBearer, self).__init__(auto_error=auto_error)

    # Authorization Middleware appled
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(AuthBearer, self).__call__(request)
        # Converting Class to Dict to check 'Bearer' token type .
        dict_credentials = dict(credentials)
        if credentials:
            if not dict_credentials['scheme'] == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid Authentication type.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403, detail="Invalid authorization code.")

    # Checking Token is Valid for Valid User
    def verify_jwt(self, jwt_token: str) -> bool:
        isValid: bool = False
        try:
            payload = decodeJWT(jwt_token)
        except:
            payload = None
        if payload:
            isValid = True
        return isValid
