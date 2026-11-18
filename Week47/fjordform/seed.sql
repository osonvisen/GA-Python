-- Optional test data for anyone who runs out of time in part 4.
-- Run fjordform_setup.sql first, so the ids start at 1.

USE fjordform;

INSERT INTO product (name, description, monthly_price) VALUES
    ('Basic',            'Tilgang til treningssalen',          399.00),
    ('Gruppetrening',    'Alle gruppetimer pluss trening',     549.00),
    ('Personlig trener', 'Ukentlig time med personlig trener', 1299.00);

INSERT INTO employee (first_name, last_name, role, email) VALUES
    ('Sara',   'Lunde', 'Personlig trener', 'sara@fjordform.example'),
    ('Henrik', 'Berg',  'Resepsjon',        'henrik@fjordform.example');

INSERT INTO customer (first_name, last_name, email, phone, product_id, trainer_id) VALUES
    ('Mona',   'Aas',    'mona@example.com',   '90011223', 1, NULL),
    ('Kjetil', 'Dahl',   'kjetil@example.com', NULL,       2, NULL),
    ('Lise',   'Moe',    'lise@example.com',   '91122334', 3, 1),
    ('Ahmed',  'Hassan', 'ahmed@example.com',  '92233445', 1, NULL),
    ('Ingrid', 'Solberg','ingrid@example.com', NULL,       2, NULL);

-- Check: number of customers per product.
SELECT p.name, COUNT(*) AS customers
FROM customer c
JOIN product p ON p.id = c.product_id
GROUP BY p.name;
