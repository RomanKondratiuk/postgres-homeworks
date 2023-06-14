-- SQL-команды для создания таблиц

CREATE TABLE customers
(
	customer_id varchar(100) PRIMARY KEY,
	company_name varchar (100),
	contact_name varchar (100)
);

--SELECT * FROM customers;



CREATE TABLE employees
(
	employee_id int primary key,
	first_name varchar (100),
	last_name varchar (100),
	title varchar (100),
	birth_date text,
    notes text
);
SELECT * FROM employees;

CREATE TABLE orders
(
    order_id int PRIMARY KEY,
	customer_id varchar (100) REFERENCES customers(customer_id),
    employee_id int REFERENCES employees(employee_id),
    order_date text,
    ship_city text
);
SELECT * FROM orders;