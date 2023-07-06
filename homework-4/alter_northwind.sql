-- Подключиться к БД Northwind и сделать следующие изменения:
-- 1. ALTER TABLE products
ADD CONSTRAINT check_unit_price_positive CHECK (unit_price > 0);


-- 2. ALTER TABLE products
ALTER TABLE products
ADD CONSTRAINT chk_products_discontinued CHECK (discontinued IN (0, 1));


-- 3. Создать новую таблицу, содержащую все продукты, снятые с продажи (discontinued = 1)
SELECT * INTO new_products FROM products WHERE discontinued = 1;


-- 4. Удалить из products товары, снятые с продажи (discontinued = 1)
-- Для 4-го пункта может потребоваться удаление ограничения, связанного с foreign_key. Подумайте, как это можно решить, чтобы связь с таблицей order_details все же осталась.
DELETE FROM order_details
WHERE product_id IN (
    SELECT product_id
    FROM products
    WHERE discontinued = 1
);

UPDATE order_details
SET product_id = NULL
WHERE product_id IN (
    SELECT product_id
    FROM products
    WHERE discontinued = 1
);

DELETE FROM products
WHERE discontinued = 1;