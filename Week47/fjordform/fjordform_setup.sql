-- Fjordform: creates the database and three empty tables.
-- Safe to run again: existing tables are dropped first (all data is lost).

CREATE DATABASE IF NOT EXISTS fjordform CHARACTER SET utf8mb4;
USE fjordform;

-- customer references product and employee, so it must be dropped first.
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS product;

CREATE TABLE product (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    name          VARCHAR(50)  NOT NULL,
    description   VARCHAR(200) NOT NULL DEFAULT '',
    monthly_price DECIMAL(8,2) NOT NULL
);

CREATE TABLE employee (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50)  NOT NULL,
    last_name  VARCHAR(50)  NOT NULL,
    role       VARCHAR(50)  NOT NULL,
    email      VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE customer (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50)  NOT NULL,
    last_name  VARCHAR(50)  NOT NULL,
    email      VARCHAR(100) NOT NULL UNIQUE,
    phone      VARCHAR(20)  NULL,
    product_id INT          NOT NULL,
    trainer_id INT          NULL,
    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (trainer_id) REFERENCES employee(id) ON DELETE SET NULL
);

-- Test: should return zero rows and no errors.
SELECT * FROM product;
