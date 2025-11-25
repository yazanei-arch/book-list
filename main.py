from fastapi import FastAPI, HTTPException

app = FastAPI()

books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
    {"id": 2, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "year": 1999},
    {"id": 3, "title": "Introduction to Algorithms", "author": "Thomas H. Cormen", "year": 2009},
    {"id": 4, "title": "Python Crash Course", "author": "Eric Matthes", "year": 2015},
    {"id": 5, "title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015},
    {"id": 6, "title": "Design Patterns", "author": "Erich Gamma", "year": 1994},
    {"id": 7, "title": "You Don't Know JS", "author": "Kyle Simpson", "year": 2015},
    {"id": 8, "title": "The Clean Coder", "author": "Robert C. Martin", "year": 2011},
    {"id": 9, "title": "Soft Skills", "author": "John Sonmez", "year": 2014},
    {"id": 10, "title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "year": 2015}
]

counter = 10


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def add_book(book: dict):
    global counter
    new_book = {
        "id": counter,
        "title": book.get("title"),
        "author": book.get("author"),
        "year":book.get("year")
    }
    books.append(new_book)
    counter += 1
    return new_book


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")