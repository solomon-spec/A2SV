# Write your MySQL query statement below
SELECT  product_name,s.year,price
FROM Sales as s
JOIN Product as p
ON s.product_id = p.product_id