from fastapi import APIRouter, Depends

from app.dal.audit import AuditDAL
from app.dal.book_item import BookItemDAL
from app.dal.books import BookDAL
from app.dal.user import UserDAL
from app.models.audits import AssignBook, ReturnBook
from app.service.audit import AuditService


router = APIRouter()

def get_audit_service():
    return AuditService(UserDAL(),BookDAL(),BookItemDAL(),AuditDAL())

@router.post("")
async def assign_book(request:AssignBook,audit_service:AuditService = Depends(get_audit_service)):
    return await audit_service.assign_book(request.model_dump())

@router.patch("")
async def return_book(request:ReturnBook,audit_service:AuditService = Depends(get_audit_service)):
    return await audit_service.return_book(request.model_dump())


@router.get("")
async def get_audits(book_item_id:int,status:str,book_id:int=None,user_id:int=None,audit_service:AuditService = Depends(get_audit_service)):
    return await audit_service.get_audits(book_id,user_id)