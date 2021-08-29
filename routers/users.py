from models.users import UserLoginSchema, UserSchema
from fastapi.routing import APIRouter
from auth.auth_handler import signJWT

# Router Initialization...
router = APIRouter()
auth_tags = ['User Auth Routes']
users_tags = ['Users Routes']


@router.post('/user/register', tags=auth_tags)
async def register_user(user: UserSchema):
    return signJWT(user.email)


@router.post('/user/login', tags=auth_tags)
async def login_user(user: UserLoginSchema):
    if checkUser(user):
        return signJWT(user.email)
    else:
        print('ERROR, Invalid credentials')
        return {
            'error': "Invalid user credentials"
        }


def checkUser(data: UserLoginSchema) -> bool:
    # Fetching From database ...
    user = {
        'email': 'admin@admin.com',
        "password": 'password'
    }
    return (user['email'] == data.email and user['password'] == data.password)


@router.get('/users', tags=users_tags)
def users() -> dict:
    return {"message": "All available users are here."}
