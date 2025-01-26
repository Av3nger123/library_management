from datetime import datetime
from typing import Dict

from app.models.audits import Audit


audit_records: Dict[int,Audit]= {}
audit_seq = 1

class AuditDAL:

    async def get_audits(self):
        return audit_records

    async def get_audits_by_filters(self,book_id=None, book_item_id=None, user_id=None, status=None):
        # Unoptimized
        final = list(audit_records.values())
        if user_id is not None:
            final = [record for record in final if record.user_id == user_id]
        if book_id is not None:
            final = [record for record in final if record.book_id == book_id]
        if book_item_id is not None:
            final = [record for record in final if record.book_item_id == book_item_id]
        if status is not None:
            final = [record for record in final if record.status == status]
        return final

    async def create_audit(self,audit:dict):
        global audit_seq
        audit_record = Audit(id=audit_seq,**audit)
        audit_records[audit_record.id] = audit_record   
        audit_seq = audit_seq + 1
        return audit_record

    async def update_audit(self, audit:dict):
        # Always should give 1 record
        if audit['id'] not in audit_records:
            return None
        audit_record = audit_records[audit['id']]
        for key, value in audit.items():
            if value is not None:
                setattr(audit_record, key, value)
        setattr(audit_record,"updated_at", datetime.now())
        audit_records[audit['id']] = audit_record  
        return audit_record 
