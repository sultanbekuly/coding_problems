-- Write your MySQL query statement below

SELECT
  t.request_at AS Day
  ,COUNT(CASE WHEN t.status = 'completed' THEN 1 ELSE NULL END) as count_completed
  ,COUNT(*)  as count_all
  ,CAST(
    ROUND( 
      1 - ( COUNT(CASE WHEN t.status = 'completed' THEN 1 ELSE NULL END) / COUNT(*) ), 
      2) AS DECIMAL(3,2) ) AS Cancellation Rate

FROM Trips t
JOIN Users u
  ON t.client_id = u.users_id
JOIN Users u2
  ON t.driver_id = u2.users_id
WHERE u.banned = 'NO' AND u2.banned = 'NO'
  AND DATEDIFF(t.request_at, '2013-10-02') <= 1
GROUP BY t.request_at