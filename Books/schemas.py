from pydantic import constr, BaseModel

class AddBook(BaseModel):
    book_name: str
    auther_name: str 
    category: str
    

class UpdateBook(BaseModel):
    book_id : int
    book_name : str
    auther_name: str
    category : str
    
class DeleteBook(BaseModel):
    book_id : int