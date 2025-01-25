
from typing import Dict

from app.models.schema import Audit


audit_records: Dict[int,Dict[int,Audit]] = {}

class AuditDAL:
    
    async def get_audits(self):
        return audit_records
        
    async def get_audits_by_user(self,user_id):
        return audit_records[user_id]
    
    async def save_audit(self,audit):
        if audit.user_id not in audit_records:
            audit_records[audit.user_id] = {}
        audit_records[audit.user_id][audit.book_id] = audit
        return audit   
