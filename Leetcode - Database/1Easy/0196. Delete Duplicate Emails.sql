-- Please write a DELETE statement and DO NOT write a SELECT statement.
-- Write your MySQL query statement below
DELETE
p1
FROM Person p1
INNER JOIN
  (SELECT email, COUNT(*) as num_of_dup, MIN(id) min_id
  FROM Person
  GROUP BY email
  HAVING COUNT(*) > 1) p2
  ON p1.email = p2.email AND p1.id != p2.min_id

