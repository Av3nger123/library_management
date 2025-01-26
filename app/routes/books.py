from fastapi import APIRouter, Depends

from app.dal.book_item import BookItemDAL
from app.dal.books import BookDAL
from app.models.books import BookCreate, BookItemCreate, BookUpdate
from app.service.books import BookService

router = APIRouter()

def get_book_service():
    return BookService(BookDAL(),BookItemDAL())

@router.get("/", response_model=None)
async def get_books(book_service: BookService = Depends(get_book_service)):
    return await book_service.get_books()

@router.get("/{id}", response_model=None)
async def get_book(id: int, book_service: BookService = Depends(get_book_service)):
    return await book_service.get_book(id)

@router.post("/", response_model=None)
async def create_books(request: BookCreate, book_service: BookService = Depends(get_book_service)):
    return await book_service.create_book(request.model_dump())

@router.patch("/{id}", response_model=None)
async def update_books(id: int, book: BookUpdate, book_service: BookService = Depends(get_book_service)):
    return await book_service.update_book(id, book.model_dump())

@router.get("/{id}/items", response_model=None)
async def get_book_items(id:int,book_service: BookService = Depends(get_book_service)):
    return await book_service.get_book_items_for_book(id)

@router.post("/items", response_model=None)
async def create_book_items(request: BookItemCreate, book_service: BookService = Depends(get_book_service)):
    return await book_service.create_book_item(request.model_dump())

