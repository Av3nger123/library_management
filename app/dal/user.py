
from app.models.schema import User


user_records = {}
user_seq = 1

class UserDAL:
        
    async def get_users(self):
        return list(user_records.values())
    
    async def get_user(self, user_id):
        return user_records[user_id]
        
    async def create_user(self,user:User):
        global user_seq
        user.id = user_seq 
        user_records[user.id] = user   
        user_seq = user_seq + 1
        return user
    
    async def update_user(self,user:User):
        user_records[user.id] = user   
        return user
    