from auth.auth_checker import AuthBearer
from fastapi import APIRouter
from fastapi import Depends

router = APIRouter()


@router.get('/posts', dependencies=[Depends(AuthBearer())],  tags=["posts"])
def posts() -> dict:
    posts = [
        {
            "id": 1,
            "title": "An dummy title",
            "description": "An dummy description"
        }
    ]
    return {
        "posts": posts
    }
