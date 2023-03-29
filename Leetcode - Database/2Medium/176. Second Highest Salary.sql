-- Write your MySQL query statement below
SELECT 
  MAX(salary) as SecondHighestSalary 
from employee 
where salary < (select max(salary) from employee)
