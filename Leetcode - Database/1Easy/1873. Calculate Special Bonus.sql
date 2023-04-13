/* Write your T-SQL query statement below */
SELECT employee_id
,CASE WHEN employee_id%2=1 AND LEFT([name], 1) != 'M' THEN salary
  ELSE 0 END AS bonus
FROM Employees
ORDER BY employee_id




-------------------------------------------------------

-- Write your MySQL query statement below
SELECT
employee_id
,CASE 
    WHEN employee_id%2 = 1 AND name NOT LIKE "M%" THEN salary --LEFT(name, 1) != 'M'
    ELSE 0 
    END AS BONUS
FROM Employees
ORDER BY employee_id