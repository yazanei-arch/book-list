from fastapi import FastAPI, HTTPException

app = FastAPI()

# רשימת ספרים בזיכרון
books = [
    {"id": 1, "title": "Harry Potter", "author": "J. K. Rowling"},
    {"id": 2, "title": "The Hobbit", "author": "J. R. R. Tolkien"},
]
counter = len(books) + 1


# a. GET /books – החזרת כל הספרים
@app.get("/books")
def get_books():
    return books


# b. GET /books/{id} – החזרת ספר לפי מזהה
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


# c. POST /books – הוספת ספר חדש (JSON עם title ו-author)
@app.post("/books")
def add_book(book: dict):
    global counter
    new_book = {
        "id": counter,
        "title": book.get("title"),
        "author": book.get("author"),
    }
    books.append(new_book)
    counter += 1
    return new_book


# d. DELETE /books/{id} – מחיקת ספר לפי מזהה
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
