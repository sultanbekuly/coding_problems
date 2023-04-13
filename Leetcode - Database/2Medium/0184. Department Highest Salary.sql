-- Write your MySQL query statement below
SELECT 
    d.name AS Department
    ,e.name AS Employee
    ,e.salary AS Salary
    FROM 
        Employee e
    INNER JOIN
        (SELECT e.departmentId ,MAX(e.salary) AS dep_max_salary
        FROM Employee e
        GROUP BY e.departmentId) e_max
        ON e.departmentId = e_max.departmentId AND e.salary = e_max.dep_max_salary
    INNER JOIN 
        Department d
        ON e.departmentId = d.id

SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN
    (SELECT departmentId, MAX(salary)
     FROM Employee
     GROUP BY departmentId)
ORDER BY Department;
