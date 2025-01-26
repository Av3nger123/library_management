
from dataclasses import dataclass
from app.dal import user, book_item, books, audit
from app.models.books import BookStatus

BOOK_LIMIT = 5

status_map = {
    "good": BookStatus.AVAILABLE,
    "bad": BookStatus.DAMAGED,
}

@dataclass
class AuditService:
    user_dal: user.UserDAL
    book_dal: books.BookDAL
    book_item_dal: book_item.BookItemDAL
    audit_dal: audit.AuditDAL
    
    async def assign_book(self,payload):
        
        user = await self.user_dal.get_user(payload['user_id'])
        if not user:
            return "User not found"
        if user.is_blocked:
            return "User is blocked"
        
        book = await self.book_dal.get_book(payload["book_id"])
        if not book:
            return "Book not found"
        
        audit_records = await self.audit_dal.get_audits_by_filters(user_id=user.id,status=BookStatus.ASSIGNED)
        if len(audit_records) >= BOOK_LIMIT:
            return f"Not allowed as the limit {BOOK_LIMIT} reached"
        
        if book_items := await self.book_item_dal.get_book_items_for_book(book.id):
            filtered = [item for item in book_items if item.status == BookStatus.AVAILABLE]
        if len(filtered) > 0:
            item = filtered[0]
            await self.book_item_dal.change_status(item.id,"assigned")
            return await self.audit_dal.create_audit({"book_item_id":item.id,**payload})
        else:
            return "No books available"
    
    async def return_book(self,payload):
        audit_record =  await self.audit_dal.update_audit({**payload,"status":"returned"})
        if not audit_record:
            return "No Audit record found"
        await self.book_item_dal.change_status(audit_record.book_item_id,status_map.get(payload.get("condition"),BookStatus.AVAILABLE))
        return audit_record

    
    async def get_audits(self,book_id=None,user_id=None,book_item_id=None,status=None):
        return await self.audit_dal.get_audits_by_filters(book_id=book_id,user_id=user_id,book_item_id=book_item_id,status=status)