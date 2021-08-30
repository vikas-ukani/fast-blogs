from fastapi import APIRouter

router = APIRouter()
tags_default = ['Default Routes']


@router.get('/main', tags=tags_default)
def main() -> dict:
    return {"message": "Main Default Route loaded..."}
