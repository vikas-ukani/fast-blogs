import uvicorn
from fastapi import FastAPI
from routers import (route, users, posts)

app = FastAPI()

app.include_router(route.router)
app.include_router(users.router)
app.include_router(posts.router)


@app.get('/', tags=['root'])
async def index() -> dict:
    return {
        "message": " Index loaded;"
    }

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
