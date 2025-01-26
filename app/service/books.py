
from dataclasses import dataclass
from app.dal.audit import AuditDAL
from app.dal.book_item import BookItemDAL
from app.dal.books import BookDAL
from app.models.books import BookItemCreate
from app.models.audits import Audit


@dataclass
class BookService:
    
    audit_dal:AuditDAL
    book_dal:BookDAL
    book_item_dal:BookItemDAL
    
    async def get_books(self):
        return await self.book_dal.get_books()
    
    async def search_books(self,q:str):
        return await self.book_dal.search_books(q)
    
    async def get_book(self,book_id):
        if book := await self.book_dal.get_book(book_id):
            book_items = await self.book_item_dal.get_book_items_for_book(book.id)
            return {**book.model_dump(),"available_items":book_items}
        return "No Book Found"
            
    async def create_book(self,payload:dict):
        book = await self.book_dal.create_book(payload)
        # Default create an item if we are create a book record
        book_item = BookItemCreate(book_id=book.id)
        await self.book_item_dal.create_book_item(book_item.model_dump())
        return book


    async def update_book(self,book_id,payload,override=False):
        book_items = await self.book_item_dal.get_book_items_for_book(book_id)
        if book_items and not override:
            return "There are book items for this book, pass override in query as true if you want to change the book attributes if you wish to continue"
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
        
    async def update_book_item(self,payload):
        if book_item := await self.book_item_dal.change_status(**payload):
            if payload['status'] == 'lost':
                if audits := await self.audit_dal.get_audits_by_filters(book_item_id=book_item.id, status="assigned"):
                    audit = audits[0]
                    audit.condition = "lost"
                    await self.audit_dal.update_audit(audit.model_dump())
            return book_item
        return f"No Book item found for this id: {payload['id']}"
        
