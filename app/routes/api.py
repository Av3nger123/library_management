from fastapi import APIRouter
from app.routes import user, books


router = APIRouter()

router.include_router(user.router,tags=['user'],prefix='/users')
router.include_router(books.router,tags=['books'])