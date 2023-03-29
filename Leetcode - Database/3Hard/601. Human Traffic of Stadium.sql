-- Write your MySQL query statement below
SELECT
s4.id
,s4.visit_date
,s4.people
FROM
Stadium s4
INNER JOIN
  (SELECT
  s1.id as s1_id
  ,s2.id as s2_id
  ,s3.id as s3_id
  FROM Stadium s1
  INNER JOIN Stadium s2
  ON s1.id = s2.id-1
  INNER JOIN Stadium s3
  ON s2.id = s3.id-1
  WHERE s1.people >= 100 AND s2.people >= 100 AND s3.people >= 100) s5
ON s4.id = s5.s1_id OR s4.id = s5.s2_id OR s4.id = s5.s3_id
GROUP BY s4.id ,s4.visit_date ,s4.people
ORDER BY s4.visit_date ASC