from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from typing import Optional

class BookStatus(Enum):
    AVAILABLE = "available"
    ASSIGNED = "assigned"
    LOST = "lost"
    DAMAGED = "damaged"

class BookBase(BaseModel):
    name: str
    author: str
    publisher: str

class Book(BookBase):
    id: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    class Config:
        orm_mode = True

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    
class BookItemBase(BaseModel):
    book_id: int
    status: BookStatus = "available"

    
class BookItem(BookItemBase):
    id:int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    class Config:
        orm_mode = True
class BookItemCreate(BookItemBase):
    pass

class BookItemUpdate(BaseModel):
    id: int
    status: str = "available"
