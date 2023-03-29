-- Write your MySQL query statement below
SELECT
t1.id
,CASE 
    WHEN t1.p_id IS NULL THEN 'Root' 
    WHEN t5.id IS NOT NULL THEN 'Inner' 
    ELSE 'Leaf' END AS type
FROM Tree t1
LEFT JOIN
    (SELECT
    t3.id
    FROM Tree t2
    INNER JOIN Tree t3
    ON t2.id = t3.p_id
    INNER JOIN Tree t4
    ON t3.id = t4.p_id
    GROUP BY t3.id) t5
ON t1.id = t5.id

