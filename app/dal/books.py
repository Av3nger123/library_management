
from typing import Dict
from app.models.schema import Book


book_records:Dict[int, Book]= {}
book_seq = 1

class BookDAL:
    
    async def search_books(self, q:str):
        found_books = []
        for book in book_records.values():
            if book.name.startswith(q):
                found_books.append(book)
        return found_books
    
    async def get_book(self, book_id):
        if book_id not in book_records:
            return None
        return book_records[book_id]


    async def get_books(self):
        return list(book_records.values())
      
    async def create_book(self,book:Book):
        global book_seq
        book.id = book_seq 
        book_records[book.id] = book   
        book_seq = book_seq + 1
        return book
    
    async def update_book(self,book:Book):
        book_records[book.id] = book   
        return book
    