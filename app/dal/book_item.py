
from datetime import datetime
from typing import Dict, List

from app.models.books import BookItem


book_item_records: Dict[int, BookItem] = {}
book_items_map: Dict[int, List[int]] = {} 
book_item_seq = 1

class BookItemDAL:
    
    async def create_book_item(self, book_item: dict):
        global book_item_seq
        book_item_record = BookItem(id=book_item_seq, **book_item)
        
        if book_item["book_id"] not in book_items_map:
            book_items_map[book_item["book_id"]] = []
            
        book_items_map[book_item["book_id"]].append(book_item_seq)
        book_item_records[book_item_seq] = book_item_record   
        
        book_item_seq = book_item_seq + 1
        return book_item_record

    async def get_book_items_for_book(self,book_id:int):
        if book_id in book_items_map:
            return [book_item_records[x] for x in book_items_map[book_id]]
        return None
    
    async def change_status(self,book_item_id:int,status:str):
        if book_item := book_item_records[book_item_id]:
            book_item.status = status
            book_item.updated_at = datetime.now()
            book_item_records[book_item_id] = book_item
            return book_item
        return None