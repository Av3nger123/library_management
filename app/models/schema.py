
from datetime import datetime
from pydantic import BaseModel


class Base(BaseModel):
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    
class User(Base):
    id:int
    name:str
    email:str
    is_blocked:bool = False
    
    class Config:
        orm_mode = True