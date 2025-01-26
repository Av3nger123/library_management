
from datetime import datetime
from typing import Dict
from app.models.users import User, UserCreate, UserUpdate


user_records: Dict[int,User] = {}
user_seq = 1

class UserDAL:
        
    async def get_users(self):
        return list(user_records.values())
    
    async def get_user(self, user_id):
        if user_id in user_records:
            return user_records[user_id]
        return None
        
    async def create_user(self,user:dict):
        global user_seq
        user_record = User(id=user_seq,**user)
        user_records[user_record.id] = user_record   
        user_seq = user_seq + 1
        return user_record
    
    async def update_user(self,user_id, user:dict):
        if user_record := user_records.get(user_id):
            for key, value in user.items():
                if value is not None:
                    setattr(user_record, key, value)
            setattr(user_record,"updated_at",datetime.now())
            user_records[user_id] = user_record  
            return user_record 
        return None
    