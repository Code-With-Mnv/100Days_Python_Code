import sqlite3

db = sqlite3.connect("books_collection.db")
cursor = db.cursor()

cursor.execute(
    "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
)

cursor.execute(
    "INSERT INTO books (id, title, author, rating) VALUES (1, 'Harry Potter', 'J.K.ROWLING', '9.3')"
)

db.commit()
