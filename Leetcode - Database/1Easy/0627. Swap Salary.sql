--# Write your MySQL query statement 
UPDATE Salary
SET sex = 
  CASE 
    WHEN sex='m' THEN 'f'
    WHEN sex='f' THEN 'm'
  END

----------------

/* Write your T-SQL query statement below */
UPDATE Salary 
SET sex = 
    CASE WHEN sex = 'm' THEN 'f'
    ELSE 'm' END
