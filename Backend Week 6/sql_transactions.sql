CREATE TABLE products (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	code TEXT UNIQUE NOT NULL,
    description TEXT NOT NULL,
	price INTEGER NOT NULL DEFAULT 0,
	qty INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
	email TEXT UNIQUE NOT NULL
);


CREATE TABLE invoices(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL CHECK (date GLOB '[0-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]'),
	amount INTEGER DEFAULT 0,
    status TEXT DEFAULT 'completed',
	user_id INTEGER NOT NULL REFERENCES users(id)
);

CREATE TABLE invoice_details(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	invoice_id INTEGER NOT NULL REFERENCES invoices(id),
    product_id INTEGER NOT NULL REFERENCES products(id),
	qty INTEGER NOT NULL DEFAULT 1,
    unit_price INTEGER NOT NULL,
    sub_total INTEGER NOT NULL DEFAULT 0
);

--transaccion de compra
BEGIN TRANSACTION;
--validacion de stock
IF NOT EXISTS ( 
SELECT 1 FROM products WHERE id = 2 AND qty > 0) THEN
    RETURN;
END IF;
--validacion de usuario
IF NOT EXISTS (
SELECT 1 FROM users WHERE id = 2 ) THEN
    RETURN;
END IF;

--creacion del invoice
INSERT INTO invoices(date,amount,status,user_id) 
VALUES (CURRENT_DATE,100,'pending',2);

-- insertar detalle
INSERT INTO invoice_details(invoice_id, product_id, qty, unit_price, sub_total)
VALUES (last_insert_rowid(), 2, 1, 100, 100);

SAVEPOINT invoice_created;

--actualizacion del inventario
UPDATE products
SET qty=qty-1
WHERE id=2;

COMMIT;

--Transaccion de devolucion
BEGIN TRANSACTION;

--Validacion de invoice existente
IF NOT EXISTS ( 
SELECT 1 FROM invoices
WHERE id = 5) THEN
    RETURN ;
END IF;
--actualiza el inventario
UPDATE products
SET qty = qty + (
    SELECT qty
    FROM invoice_details
    WHERE invoice_id = 5
)
WHERE id = (
    SELECT product_id
    FROM invoice_details
    WHERE invoice_id = 5
);
--actualiza el estado de la factura 
UPDATE invoices 
SET status = 'returned'
WHERE id=5;
COMMIT;