
from dataclasses import dataclass
from app.dal.user import UserDAL

@dataclass
class UserService:
    user_dal: UserDAL
    
    async def get_user(self,user_id:int):
        return await self.user_dal.get_user(user_id)
    
    async def get_users(self):
        return await self.user_dal.get_users()
    
    async def create_user(self,payload:dict):
        return await self.user_dal.create_user(payload)

    async def update_user(self, user_id, payload:dict):
        if user_record := await self.user_dal.update_user(user_id,payload):
            return user_record
        return f"No User found for this user_id: {user_id}"