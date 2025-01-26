from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class AuditBase(BaseModel):
    user_id: int
    book_id:int
    status:str = "assigned"

    
class Audit(AuditBase):
    id: int
    book_item_id: int  
    condition: Optional[str] = ""
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    
    class Config:
        orm_mode = True

class AssignBook(AuditBase):
    pass

class ReturnBook(BaseModel):
    id:int
    condition: str = "good"




