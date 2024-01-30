-- SQLite
CREATE TABLE clients (
    id INTEGER PRIMARY KEY  AUTOINCREMENT,
    vardas VARCHAR(50),
    pavarde VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(30)
);

ALTER TABLE clients ADD address TEXT(1000);
DROP TABLE clients;

