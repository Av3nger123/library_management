from datetime import datetime
from pydantic import BaseModel
from typing import Optional

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
    status: str = "available"
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    
class BookItem(BookItemBase):
    id:int
    class Config:
        orm_mode = True
class BookItemCreate(BookItemBase):
    pass