from fastapi import APIRouter, Depends

from app.dal.book_item import BookItemDAL
from app.dal.books import BookDAL
from app.models.books import BookCreate, BookItemCreate, BookItemUpdate, BookUpdate
from app.service.books import BookService

router = APIRouter()

def get_book_service():
    return BookService(BookDAL(),BookItemDAL())


@router.get("/{id}/items", response_model=None)
async def get_book_items(id:int,book_service: BookService = Depends(get_book_service)):
    return await book_service.get_book_items_for_book(id)

@router.post("/items", response_model=None)
async def create_book_item(request: BookItemCreate, book_service: BookService = Depends(get_book_service)):
    return await book_service.create_book_item(request.model_dump())

@router.patch("/items", response_model=None)
async def update_book_item(request: BookItemUpdate, book_service: BookService = Depends(get_book_service)):
    return await book_service.update_book_item(request.model_dump())

@router.get("/", response_model=None)
async def get_books(book_service: BookService = Depends(get_book_service)):
    return await book_service.get_books()

@router.get("/search", response_model=None)
async def get_books(q: str, book_service: BookService = Depends(get_book_service)):
    return await book_service.search_books(q)
@router.get("/{id}", response_model=None)
async def get_book(id: int, book_service: BookService = Depends(get_book_service)):
    return await book_service.get_book(id)
@router.post("/", response_model=None)
async def create_book(request: BookCreate, book_service: BookService = Depends(get_book_service)):
    return await book_service.create_book(request.model_dump())

@router.patch("/{id}", response_model=None)
async def update_book(id: int, book: BookUpdate, book_service: BookService = Depends(get_book_service)):
    return await book_service.update_book(id, book.model_dump())


