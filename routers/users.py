from pydantic import BaseModel
from models.users import UserLoginSchema, UserSchema
from fastapi.routing import APIRouter
from auth.auth_handler import signJWT
from fastapi import Body


router = APIRouter()


@router.post('/user/register', tags=['user'])
async def register_user(user: UserSchema):
    return signJWT(user.email)


@router.post('/user/login', tags=['user'])
async def login_user(user: UserLoginSchema):
    if checkUser(user):
        return signJWT(user.email)
    else:
        print('ERORO, Invalid credentials')
        return {
            'error': "Invalid user credentials"
        }


def checkUser(data: UserLoginSchema) -> bool:
    user = {
        'email': 'admin@admin.com',
        "password": 'password'
    }
    if user['email'] == data.email and user['password'] == data.password:
        return True
    return False


@router.get('/users')
def users():
    return {"message": "All available users are here."}
