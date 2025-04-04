from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends
from Books.schemas import AddBook, UpdateBook, DeleteBook
from Books.models import Books
from Books.services import BookService
from utils.database import get_db

router = APIRouter()

class BooksAPI:
    @router.post("/create_books")
    def create_book(book: AddBook, db : Session = Depends(get_db)):
        return BookService.create_book(book, db)
    
    @router.get("/get_book")
    def get_book(db : Session = Depends(get_db)):
        return BookService.get_book(db)

    @router.put("/update_book")
    def update_book(data: UpdateBook, db : Session = Depends(get_db)):
        return BookService.update_book(data, db)

    @router.delete("/delete_book")
    def delete_book(data: DeleteBook, db: Session = Depends(get_db)):
        return BookService.delete_book(data, db)