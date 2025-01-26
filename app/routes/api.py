from fastapi import APIRouter
from app.routes import books, users, audits


router = APIRouter()

router.include_router(users.router,tags=['user'],prefix='/users')
router.include_router(books.router,tags=['books'],prefix='/books')
router.include_router(audits.router,tags=['audits'],prefix='/audits')