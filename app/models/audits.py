from datetime import datetime
from typing import Optional
from pydantic import BaseModel, root_validator, validator

class AuditBase(BaseModel):
    user_id: int
    book_id: int
    status: str = "assigned"

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
    id: int
    status: str = "returned"
    condition: str = "good"
    
    @root_validator(pre=True)
    def check_status_and_condition(cls, values):
        status = values.get('status')
        condition = values.get('condition')
        if status == "lost":
            values['condition'] = None
        elif status == 'returned' and condition not in ['good','bad']:
            raise ValueError("Condition can only be 'good' or 'bad'")
        elif status and status not in ['returned','lost'] :
            raise ValueError("Status can only be 'returned' or 'lost'")
        return values




