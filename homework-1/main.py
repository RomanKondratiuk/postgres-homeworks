# """Скрипт для заполнения данными таблиц в БД Postgres."""


import csv
import psycopg2

"""Скрипт для заполнения данными таблиц в БД Postgres."""

# подключение к Б/Д
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='20010906')

# create table customers
try:
    with conn:
        with conn.cursor() as cursor:
            # Внесение данных из файла CSV в таблицу "customers"
            with open('north_data/customers_data.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute(
                        "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
                        row
                    )
finally:
    conn.commit()
    # conn.close()


# create table employees
try:
    with conn:
        with conn.cursor() as cursor:
            # Внесение данных из файла CSV в таблицу "employees"
            with open('north_data/employees_data.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute(
                        "INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes)"
                        " VALUES (%s, %s, %s, %s, %s, %s)",
                        row
                    )
finally:
    conn.commit()
    # conn.close()



# create table orders
try:
    with conn:
        with conn.cursor() as cursor:
            # Внесение данных из файла CSV в таблицу "orders"
            with open('north_data/orders_data.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute(
                        "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city)"
                        " VALUES (%s, %s, %s, %s, %s)",
                        row
                    )
finally:
    conn.commit()
    conn.close()

