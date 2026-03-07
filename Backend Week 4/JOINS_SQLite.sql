-- SQLite
DROP TABLE books;
DROP TABLE authors;
DROP TABLE customers;
DROP TABLE rents;

PRAGMA foreign_keys = ON;


CREATE TABLE books (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT UNIQUE NOT NULL,
    author_id INTEGER REFERENCES authors(id) DEFAULT NULL
);

CREATE TABLE authors (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
);

CREATE TABLE customers(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
    email TEXT DEFAULT NULL
);

CREATE TABLE rents (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	book_id INTEGER REFERENCES books(id),
    customer_id INTEGER REFERENCES customers(id),
    state TEXT DEFAULT 'Returned'
);


-- Insertar autores
INSERT INTO authors (id, name) VALUES
(1, 'Miguel de Cervantes'),
(2, 'Dante Alighieri'),
(3, 'Takehiko Inoue'),
(4, 'Akira Toriyama'),
(5, 'Walt Disney');

-- Insertar libros
INSERT INTO books (id, name, author_id) VALUES
(1, 'Don Quijote', 1),
(2, 'La Divina Comedia', 2),
(3, 'Vagabond 1-3', 3),
(4, 'Dragon Ball 1', 4),
(5, 'The Book of the 5 Rings', NULL);

-- Insertar clientes
INSERT INTO customers (id, name, email) VALUES
(1, 'John Doe', 'j.doe@email.com'),
(2, 'Jane Doe', 'jane@doe.com'),
(3, 'Luke Skywalker', 'darth.son@email.com');

-- Insertar rentas
INSERT INTO rents (id, book_id, customer_id, state) VALUES
(1, 1, 2, 'Returned'),
(2, 2, 2, 'Returned'),
(3, 1, 1, 'On time'),
(4, 3, 1, 'On time'),
(5, 2, 2, 'Overdue');

SELECT * FROM authors;
SELECT * FROM books;
SELECT * FROM customers;
SELECT * FROM rents;

/*1.Obtenga todos los libros y sus autores*/
SELECT b.name AS book_name, b.author_id, a.name AS author_name
FROM books b
LEFT JOIN authors a ON b.author_id=a.id;

/*2.Obtenga todos los libros que no tienen autor*/
SELECT b.name AS book_name
FROM books b
WHERE b.author_id is NULL;

/*3.Obtenga todos los autores que no tienen libros*/
SELECT a.name AS authors_name
FROM authors a
LEFT JOIN books b ON a.id=b.author_id
WHERE b.author_id IS NULL;

/*4.Obtenga todos los libros que han sido rentados en algún momento*/

SELECT b.name AS book_name
FROM books b

INNER JOIN rents r ON b.id=r.book_id;

/*5.Obtenga todos los libros que nunca han sido rentados*/

SELECT b.name AS book_name
FROM books b
LEFT JOIN rents r ON b.id=r.book_id
WHERE r.book_id IS NULL;

/*6.Obtenga todos los clientes que nunca han rentado un libro*/
SELECT c.name AS customers_name
FROM customers c
LEFT JOIN rents r ON c.id=r.customer_id
WHERE r.customer_id IS NULL;

/*7.Obtenga todos los libros que han sido rentados y están en estado “Overdue”*/

SELECT b.name AS book_name
FROM books b
INNER JOIN rents r ON b.id=r.book_id
WHERE r.state = 'Overdue' ;