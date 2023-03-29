-- Write your MySQL query statement below
SELECT 
    l1.num AS ConsecutiveNums
FROM 
    Logs l1
    JOIN Logs l2
    on l1.id = (l2.id-1)
    JOIN Logs l3
    on l2.id = (l3.id-1)
where 
    l1.num = l2.num and l2.num = l3.num
group by 
    l1.num
HAVING COUNT(*) >=1

