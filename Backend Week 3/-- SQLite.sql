-- SQLite
--Para usar un autonincrement en SQLite, se debe especificar el primary ID como INTEGER y no solo INT. 


/*CREATE TABLE products (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	code VARCHAR(25) NOT NULL,
    name VARCHAR(25) NOT NULL,
	price INT DEFAULT 0,
	brand VARCHAR(50) DEFAULT 0
--)*/

/*CREATE TABLE users (
	id INT PRIMARY KEY,
	user VARCHAR(50) NOT NULL
);*/

/*-- SQLite
CREATE TABLE invoices(
	id INT PRIMARY KEY,
	invoice_number INT(25) NOT NULL,
    date TEXT NOT NULL,
	amount INT DEFAULT 0,
	user_id INT REFERENCES users(id)
);*/

/*
CREATE TABLE shopping_cart(
	id INT PRIMARY KEY,
	product_id INT REFERENCES products(id),
    qty SMALLINT NOT NULL,
	user_id INT REFERENCES users(id)
);*/

/*CREATE TABLE invoice_details(
	id INT PRIMARY KEY,
	invoice_id INT REFERENCES invoices(id),
    product_id INT REFERENCES products(id),
	qty SMALLINT NOT NULL,
    total_amount INT NOT NULL
);*/

/*INSERT INTO products (code, name, price, brand)
VALUES
('PRD-001', 'Wireless Mouse', 12500, 'Logitech'),
('PRD-002', 'Mechanical Keyboard', 58900, 'Redragon'),
('PRD-003', 'USB-C Charger', 8900, 'Anker'),
('PRD-004', 'Bluetooth Speaker', 32900, 'JBL'),
('PRD-005', '27-inch Monitor', 189000, 'Samsung'),
('PRD-006', 'External SSD 1TB', 245000, 'Kingston'),
('PRD-007', 'Gaming Headset', 49900, 'HyperX'),
('PRD-008', 'Webcam 1080p', 39900, 'Logitech'),
('PRD-009', 'Smartwatch', 92500, 'Amazfit'),
('PRD-010', 'Wireless Earbuds', 37500, 'Sony');*/

/*INSERT INTO users (id, user)
VALUES (1,'user1@yahoo.com'),
(2,'user2@yahoo.com'),
(3,'user3@yahoo.com'),
(4,'user4@yahoo.com'),
(5,'user5@yahoo.com');*/

/**/

/*INSERT INTO invoices (id, invoice_number, date, amount, user_id)
VALUES
(1, 1001, '2025-10-01', 76700, 2),
(2, 1002, '2025-10-02', 201500, 1),
(3, 1003, '2025-10-03', 89800, 3),
(4, 1004, '2025-10-04', 337500, 4),
(5, 1005, '2025-10-05', 70400, 5);*/

--Aquí desglosamos qué productos se vendieron en cada invoice, con cantidad (qty) y total (total_amount = price * qty)
/*INSERT INTO invoice_details (id, invoice_id, product_id, qty, total_amount)
VALUES
(1,  1, 2, 1, 58900),   -- Mechanical Keyboard para user2
(2, 2, 1, 1, 12500),   -- Wireless Mouse para user1
(3, 3, 7, 1, 49900),   -- Gaming Headset para user3
(4, 4, 6, 1, 245000),  -- External SSD 1TB para user4
(5, 5, 4, 1, 32900),   -- Bluetooth Speaker para user5
(6, 1, 3, 2, 17800),   -- User2 compró 2 USB-C Chargers (añadido al total si quieres)
(7, 2, 5, 1, 189000),  -- User1 compró 27-inch Monitor
(8, 3, 8, 1, 39900),   -- User3 compró Webcam 1080p
(9, 4, 9, 1, 92500),   -- User4 compró Smartwatch
(10, 5, 10, 1, 37500); -- User5 compró Wireless Earbuds*/

/*Realice los siguientes `SELECT`:
    1. Obtenga todos los productos almacenados
    2. Obtenga todos los productos que tengan un precio mayor a 50000
    3. Obtenga todas las compras de un mismo producto por id.
    4. Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
    5. Obtenga todas las facturas realizadas por el mismo comprador
    6. Obtenga todas las facturas ordenadas por monto total de forma descendente
    7. Obtenga una sola factura por número de factura.*/

SELECT *
    FROM products;

SELECT *
    FROM products WHERE price > 50000;

SELECT *
    FROM invoice_details WHERE product_id = 2;

SELECT product_id, SUM(qty) AS total_qty
FROM invoice_details
GROUP BY product_id
ORDER BY total_qty DESC;

SELECT *
    FROM invoices WHERE user_id=1;

SELECT *
    FROM invoices
    ORDER BY amount DESC;

SELECT * 
    FROM invoices
    WHERE invoice_number=1004;