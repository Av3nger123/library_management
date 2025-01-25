from fastapi import APIRouter, Depends

from app.dal.audit import AuditDAL
from app.dal.books import BookDAL
from app.dal.user import UserDAL
from app.service.books import BookService

router = APIRouter(prefix="/books")

def get_book_service():
    return BookService(UserDAL(),BookDAL(),AuditDAL())

@router.get("/")
async def get_books(book_service:BookService= Depends(get_book_service)):
    return await book_service.get_books()

@router.get("/users")
async def assign_books(book_service:BookService= Depends(get_book_service)):
    return await book_service.audit_records()

@router.get("/{id}")
async def get_book(id:int,book_service:BookService= Depends(get_book_service)):
    return await book_service.get_book(id)

@router.post("/")
async def create_books(payload:dict, book_service:BookService= Depends(get_book_service)):
    return await book_service.create_books(payload)

@router.patch("/{id}")
async def update_books(id:int,payload:dict,  book_service:BookService= Depends(get_book_service)):
    return await book_service.update_book(id,payload) 

@router.post("/users")
async def assign_books(payload:dict, book_service:BookService= Depends(get_book_service)):
    return await book_service.assign_books(payload)
