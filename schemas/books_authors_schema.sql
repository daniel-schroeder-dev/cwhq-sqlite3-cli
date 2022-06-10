DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS books;

CREATE TABLE authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_name TEXT NOT NULL
);

INSERT INTO authors (author_name)
VALUES 
    ("J.D. Salinger"),
    ("Harper Lee"),
    ("Truman Capote");

CREATE TABLE books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL REFERENCES authors (author_id),
    book_title TEXT UNIQUE NOT NULL
);

INSERT INTO books (book_title, author_id)
VALUES
    ("To Kill a Mockingbird", 2),
    ("In Cold Blood", 3),
    ("The Catcher in the Rye", 1),
    ("Breakfast at Tiffanys", 3),
    ("Franny and Zooey", 1),
    ("Summer Crossing", 3),
    ("Go Set a Watchman", 2);