from app.models.schema import Base

class UserBase(Base):
    name:str
    email:str
    is_blocked:bool = False
    
class User(UserBase):
    id:int
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass



