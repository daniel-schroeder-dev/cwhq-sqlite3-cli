DROP TABLE IF EXISTS products;

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT UNIQUE NOT NULL,
    product_price REAL NOT NULL,
    product_category TEXT NOT NULL
);

INSERT INTO products (product_name, product_price, product_category)
VALUES
    ("Dell XPS 17", 1599.99, "Computers"),
    ("Blue Snowball Microphone", 99.50, "Microphones"),
    ("System76 Thelio B1", 1255.55, "Computers"),
    ("Logitech M1", 34.99, "Accessories"),
    ("Seagate S1 SSD", 88.75, "Accessories"),
    ("MacBook Pro 16", 2100.50, "Computers"),
    ("Rode Z28", 275.99, "Microphones"),
    ("Lenovo ThinkPad", 950.75, "Computers");