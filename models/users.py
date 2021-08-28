from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    first_name: str = Field()
    last_name: str = Field()
    email: str = Field()
    password: str = Field()

    class Config():
        schema_extra = {
            'example': {
                'first_name': "Vikas",
                'last_name': "Ukani",
                'email': 'vikas@admin.com',
                'password': 'password@hash'
            }
        }


class UserLoginSchema(BaseModel):
    email: str = Field()
    password: str = Field()

    class Config():
        schema_extra = {
            "example": {
                'email': "admin@admin.com",
                'password': 'password'
            }
        }
