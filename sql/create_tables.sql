CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at CURRENT_TIMESTAMP,
    is_buyer BOOLEAN DEFAULT FALSE,
    is_cook BOOLEAN DEFAULT FALSE,
    telefonnummer TEXT,
    photo_url TEXT,
    sprachen TEXT,
    beschreibung TEXT,
    studentenwohnheim_id INTEGER,
    FOREIGN KEY (studentenwohnheim_id) REFERENCES studentenwohnheim (id) ON DELETE CASCADE
);

CREATE TABLE studentenwohnheim (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
);