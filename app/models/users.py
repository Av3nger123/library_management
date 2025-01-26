from datetime import datetime
from pydantic import BaseModel, root_validator
from typing import Optional  # Import Optional

class UserBase(BaseModel):
    name: str
    email: str
    is_blocked: bool = False
    
class User(UserBase):
    id: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None 
    email: Optional[str] = None 
    is_blocked: Optional[bool] = None

    @root_validator(pre=True)
    def check_at_least_one_field(cls, values):
        if not any(values.values()):
            raise ValueError("At least one field (name, email, is_blocked) must be provided")
        return values



