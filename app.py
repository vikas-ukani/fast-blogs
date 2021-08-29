from fastapi import FastAPI
from routers.route import router as DefaultRoutes
from routers.users import router as UserRoutes
from routers.posts import router as PostsRoutes

# Start FastAPI Application...
app = FastAPI()

# Include Routes
app.include_router(DefaultRoutes)
app.include_router(UserRoutes)
app.include_router(PostsRoutes)


# Application Default Route
@app.get('/', tags=['root'])
async def index() -> dict:
    return {"message": " Welcome to the Fast Blogs..."}
