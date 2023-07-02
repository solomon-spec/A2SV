# Write your MySQL query statement below
SELECT a.id
FROM Weather AS a
JOIN Weather AS b
ON a.recordDate = b.recordDate + INTERVAL 1 DAY
WHERE a.temperature > b.temperature;