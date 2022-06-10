DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS teachers;

CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO users (username, password) 
VALUES 
    ("djs", "mypa$$word"),
    ("django", "w0ff"),
    ("alecg", "c0de");


CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL REFERENCES users (user_id),
    username TEXT,
    password TEXT,
    is_admin INTEGER NOT NULL
);

INSERT INTO teachers (user_id, username, password, is_admin)
VALUES
    (1, "djs", "mypa$$word", 1),
    (3, "alecg", "c0de", 0);