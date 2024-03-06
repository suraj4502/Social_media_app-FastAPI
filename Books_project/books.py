from models import Book, BookRequest
from fastapi import FastAPI, Path, Query, HTTPException

from starlette import status

app = FastAPI()

BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'An awesome book!', 5, 2029),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2028),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2027),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2026)
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return {"books": BOOKS}


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0, title="The ID of the book you want to retrieve")):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')


@app.get("/books/rating/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(title="Filter books by rating", gt=0, lt=6)):
    books_to_return = [book for book in BOOKS if book.rating == book_rating]
    return books_to_return


@app.get("/books/published/", status_code=status.HTTP_200_OK)
async def read_books_by_publish_date(published_date: int = Query(title="Filter books by published date", gt=1999, lt=2031)):
    books_to_return = [book for book in BOOKS if book.published_date == published_date]
    return books_to_return


@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    new_book.id = find_book_id()
    print("NEW BOOK ::", new_book)
    BOOKS.append(new_book)
    return new_book


def find_book_id():
    return max(book.id for book in BOOKS) + 1 if BOOKS else 1


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    for i, existing_book in enumerate(BOOKS):
        if existing_book.id == book.id:
            BOOKS[i] = Book(**book.dict())
            return
    raise HTTPException(status_code=404, detail='Item not found')


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0, title="The ID of the book you want to delete")):
    for i, existing_book in enumerate(BOOKS):
        if existing_book.id == book_id:
            del BOOKS[i]
            return
    raise HTTPException(status_code=404, detail='Item not found')
