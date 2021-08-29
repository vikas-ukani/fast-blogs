from pydantic import BaseModel, Field


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(max_length=100)
    description: str = Field(max_length=255)

    class Config:
        schema_extra = {
            "example": {
                "title": "Secured with FastAPI using JWT auth token.",
                "description": "An complete description about this post."
            }
        }
