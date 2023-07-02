# Write your MySQL query statement below
SELECT customer_id,count(*) AS count_no_trans
FROM Visits AS v
LEFT OUTER JOIN Transactions AS t
ON t.visit_id  = v.visit_id 
WHERE  transaction_id IS NULL
GROUP BY customer_id;
