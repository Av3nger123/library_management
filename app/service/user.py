
from dataclasses import dataclass
from app.dal.user import UserDAL
from app.models.request import UserCreate
from app.models.schema import User

@dataclass
class UserService:
    user_dal: UserDAL
    
    async def get_user(self,user_id:int):
        return await self.user_dal.get_user(user_id)
    
    async def get_users(self):
        return await self.user_dal.get_users()
    
    async def create_user(self,payload:UserCreate):
        user = User(**payload)
        return await self.user_dal.create_user(user)

    async def update_user(self, user_id,payload):
        user = User(**payload)
        user.id = user_id
        return await self.user_dal.update_user(user)