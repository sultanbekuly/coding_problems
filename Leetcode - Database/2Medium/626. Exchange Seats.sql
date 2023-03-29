-- Write your MySQL query statement below
SELECT
s1.id
,CASE
  WHEN s1.id%2=1 AND s3.id IS NULL THEN s1.student
  WHEN s1.id%2=1 THEN s3.student
  WHEN s1.id%2=0 THEN s2.student
  ELSE s1.student END AS student
FROM Seat s1
LEFT JOIN Seat s2
ON s1.id = s2.id+1
LEFT JOIN Seat s3
ON s1.id = s3.id-1
ORDER BY s1.id ASC