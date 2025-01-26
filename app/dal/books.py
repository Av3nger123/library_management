from datetime import datetime
from typing import Dict
from app.models.books import Book

book_records: Dict[int, Book] = {}
book_seq = 1

class BookDAL:
        
    async def get_books(self):
        return list(book_records.values())
    
    async def get_book(self, book_id):
        if book_id in book_records:
            return book_records[book_id]
        return None
        
    async def create_book(self, book: dict):
        global book_seq
        book_record = Book(id=book_seq, **book)
        book_records[book_record.id] = book_record   
        book_seq = book_seq + 1
        return book_record
    
    async def update_book(self, book_id, book: dict):
        if book_record := book_records.get(book_id):
            for key, value in book.items():
                if value is not None:
                    setattr(book_record, key, value)
            setattr(book_record, "updated_at", datetime.now())
            book_records[book_id] = book_record  
            return book_record 
        return None
