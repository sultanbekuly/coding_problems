# Write your MySQL query statement below
SELECT
s.name
FROM SalesPerson s
WHERE s.name NOT IN 
    (SELECT
    s.name
    FROM Orders o
    RIGHT JOIN SalesPerson s
    ON o.sales_id = s.sales_id
    LEFT JOIN Company c
    ON o.com_id = c.com_id
    WHERE c.name = 'RED')

/*
| name | name   |
| ---- | ------ |
| John | RED    |
| Amy  | null   |
| Mark | null   |
| Pam  | RED    |
| Pam  | YELLOW |
| Alex | GREEN  |*/