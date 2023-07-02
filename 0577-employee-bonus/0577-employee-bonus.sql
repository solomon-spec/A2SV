# Write your MySQL query statement below
SELECT name,bonus
FROM Employee AS e
LEFT OUTER JOIN Bonus AS b
ON e.empId = b.empId
WHERE b.bonus IS NULL OR b.bonus < 1000;