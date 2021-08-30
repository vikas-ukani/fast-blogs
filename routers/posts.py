from auth.auth_checker import AuthBearer
from fastapi import APIRouter
from fastapi import Depends

# routes
router = APIRouter()
PROTECTED_ROUTE = [Depends(AuthBearer())]
tags_posts = ["Posts Routes"]


@router.get('/posts', dependencies=PROTECTED_ROUTE,  tags=tags_posts)
def posts() -> dict:
    posts = [
        {
            "id": 1,
            "title": "An dummy title",
            "description": "An dummy description"
        }
    ]
    return {
        "posts": posts,
        "message": 'All available posts.'
    }
