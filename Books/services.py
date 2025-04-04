from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends
from Books.schemas import AddBook, UpdateBook, DeleteBook
from Books.models import Books
from utils.database import get_db

router = APIRouter() 
class BookService:
    def create_book(book: AddBook, db : Session = Depends(get_db)):
        try:
            existing_books = db.query(Books).filter(Books.book_name == book.book_name).first()
            if existing_books:
                raise HTTPException(status_code=400, detail="Book are all ready Available")
            
            new_book = Books(
                book_name = book.book_name,
                auther_name = book.auther_name,
                category = book.category
            )
            db.add(new_book)
            db.commit()
            db.refresh(new_book)
            return {"message": "Create new Book Sucessfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
        
    def get_book(db : Session = Depends(get_db)):
        try:
            book_list = db.query(Books).all()
            book_data = [{  "book_name" : bk.book_name,
                            "book_id": bk.book_id,
                            "auther_name": bk.auther_name,
                            "category": bk.category} for bk in book_list]
            return {"total_book": len(book_list), "book":book_data}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
        
    def update_book(data: UpdateBook, db : Session = Depends(get_db)):
        try:
            book = db.query(Books).filter(Books.book_id == data.book_id).first()
            if not book:
                raise HTTPException(status_code=400, detail="Book is not available")
            
            existing_book = db.query(Books).filter(
                Books.book_name == data.book_name,
                Books.book_id != data.book_id
            ).first()
            
            if existing_book:
                raise HTTPException(status_code=400, detail=f"A book with name already exist")
                       
            book.book_name = data.book_name
            book.auther_name = data.auther_name
            book.category = data.category
            
            db.commit()
            db.refresh(book)
            return {"message": "update book Information"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Internal Server Error: {str(e)}")
        
    def delete_book(data: DeleteBook, db: Session = Depends(get_db)):
        try:
            book = db.query(Books).filter(Books.book_id == data.book_id).first()
            if  not book:
                raise HTTPException(status_code=400, detail="Book not Available")
            
            db.delete(book)
            db.commit()
            return {"Message" : "Delete Book Sucessfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
        