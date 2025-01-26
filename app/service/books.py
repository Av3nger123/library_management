
from dataclasses import dataclass
from app.dal.book_item import BookItemDAL
from app.dal.books import BookDAL
from app.models.books import BookItemCreate
from app.models.audits import Audit


@dataclass
class BookService:
    
    book_dal:BookDAL
    book_item_dal:BookItemDAL
    
    async def get_books(self):
        return await self.book_dal.get_books()
    
    async def get_book(self,book_id):
        return await self.book_dal.get_book(book_id)

    async def create_book(self,payload:dict):
        book = await self.book_dal.create_book(payload)
        # Default create an item if we are create a book record
        book_item = BookItemCreate(book_id=book.id)
        await self.book_item_dal.create_book_item(book_item.model_dump())
        return book


    async def update_book(self,book_id,payload):
        if book_record := await self.book_dal.update_book(book_id,payload):
            return book_record
        return f"No Book found for this book_id: {book_id}"

    async def get_book_items_for_book(self,book_id:int):
        if book_items := await self.book_item_dal.get_book_items_for_book(book_id):
            return book_items
        return f"No Book Items found for this book_id: {book_id}"
    
    async def create_book_item(self,payload):
        if book := await self.book_dal.get_book(payload['book_id']):
            return await self.book_item_dal.create_book_item(payload)
        return f"No Book found for this book_id: {payload['book_id']}"
    
    
    async def assign_books(self,payload):
        if payload['action'] == 'assign':
            if book := await self.book_dal.get_book(payload["book_id"]):
                if book.total > 0:
                    audit = Audit(user_id=payload['user_id'],book_id=payload['book_id'],status="assigned")
                    book.total = book.total - 1
                    await self.book_dal.update_book(book)
                    return await self.audit_dal.save_audit(audit)
                else:
                    return "Not allowed"
            else:
                "Book not found"
        elif payload['action'] == 'return':
            audit = Audit(user_id=payload['user_id'],book_id=payload['book_id'],status="returned")
            book = await self.book_dal.get_book(payload['book_id'])
            book.total = book.total + 1
            await self.book_dal.update_book(book)
            return await self.audit_dal.save_audit(audit)
            
    async def audit_records(self):
        return await self.audit_dal.get_audits()
        
