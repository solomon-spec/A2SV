# Write your MySQL query statement below
SELECT a.machine_id, ROUND(AVG(b.timestamp) - AVG(a.timestamp),3) AS processing_time
FROM Activity AS a
JOIN Activity AS b
ON a.machine_id = b.machine_id &&  a.process_id = b.process_id 
    && a.activity_type  = 'start' && b.activity_type  = 'end'
GROUP BY a.machine_id