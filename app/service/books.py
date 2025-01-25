
from dataclasses import dataclass
from app.dal.audit import AuditDAL
from app.dal.books import BookDAL
from app.dal.user import UserDAL
from app.models.schema import Audit, Book


@dataclass
class BookService:
    
    user_dal:UserDAL
    book_dal:BookDAL
    audit_dal:AuditDAL
    
    async def get_books(self):
        return await self.book_dal.get_books()
    
    async def get_book(self,book_id):
        return await self.book_dal.get_book(book_id)

    async def create_books(self,payload):
        book = Book(**payload)
        return await self.book_dal.create_book(book)

    async def update_book(self,book_id,payload):
        book = Book(**payload)
        book.id = book_id
        return await self.book_dal.update_book(book)

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
        
