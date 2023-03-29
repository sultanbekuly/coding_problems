-- Write your MySQL query statement below
SELECT 
    dep.name as Department
    ,emp.name as Employee
    ,emp.salary as Salary
FROM
    (SELECT 
        id
        ,name
        ,salary
        ,departmentId
        ,DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) as ranking
    FROM Employee) emp
    INNER JOIN Department dep
    ON emp.departmentId = dep.id
WHERE emp.ranking <= 3
