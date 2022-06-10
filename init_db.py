from uuid import uuid4
import sqlite3
from pathlib import Path

db_name = f"dbs/sqlite-practice-{uuid4()}.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()


def populate_db():
    with open(
        "schemas/books_authors_schema.sql", mode="rt", encoding="utf-8"
    ) as books_authors_schema_file:
        books_authors_schema = books_authors_schema_file.read()

    with open(
        "schemas/users_teachers_schema.sql", mode="rt", encoding="utf-8"
    ) as users_teachers_schema_file:
        users_teachers_schema = users_teachers_schema_file.read()

    with open(
        "schemas/products_schema.sql", mode="rt", encoding="utf-8"
    ) as products_schema_file:
        products_schema = products_schema_file.read()

    cursor.executescript(books_authors_schema)
    cursor.executescript(users_teachers_schema)
    cursor.executescript(products_schema)


def remove_db():
    Path(db_name).unlink()
