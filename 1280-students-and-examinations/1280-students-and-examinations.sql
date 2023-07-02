# Write your MySQL query statement below
SELECT st.student_id,st.student_name,su.subject_name,IFNULL(COUNT(e.student_id),0) AS  attended_exams
FROM Students st
JOIN Subjects su
LEFT OUTER JOIN Examinations e
ON e.student_id = st.student_id AND e.subject_name = su.subject_name
GROUP BY st.student_id,su.subject_name
ORDER BY st.student_id,su.subject_name