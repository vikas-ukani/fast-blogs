from fastapi import APIRouter

router = APIRouter()


@router.get('/main')
def main():
    return {"message": "Main loaded"}
