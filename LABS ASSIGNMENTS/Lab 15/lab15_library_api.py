# lab15_library_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI(
    title="Library Book Management API",
    description="RESTful API to manage library books with CRUD and partial updates.",
    version="1.0.0"
)

# ----- Data Models -----
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    available: bool = True

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    available: Optional[bool] = None

# In-memory “database”
books_db: Dict[int, Book] = {}

# ----- Endpoints -----

@app.get("/books")
def get_books():
    """
    Retrieve all books in the library.
    """
    return list(books_db.values())


@app.post("/books", response_model=Book)
def add_book(book: Book):
    """
    Add a new book to the collection.
    """
    if book.id in books_db:
        raise HTTPException(status_code=400, detail="Book ID already exists.")
    books_db[book.id] = book
    return book


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    """
    Retrieve details of a specific book by ID.
    """
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found.")
    return books_db[book_id]


@app.patch("/books/{book_id}", response_model=Book)
def update_book_partial(book_id: int, book_update: BookUpdate):
    """
    Partially update book details (e.g., availability).
    """
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found.")

    stored_book = books_db[book_id]
    updated_data = book_update.model_dump(exclude_unset=True)

    # Update only provided fields
    for key, value in updated_data.items():
        setattr(stored_book, key, value)

    books_db[book_id] = stored_book
    return stored_book


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """
    Remove a book from the collection.
    """
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found.")
    del books_db[book_id]
    return {"message": f"Book with ID {book_id} deleted successfully."}
