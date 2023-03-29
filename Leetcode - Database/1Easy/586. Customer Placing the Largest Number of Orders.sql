-- Write your MySQL query statement below
SELECT customer_number
  # ,COUNT(*) as num_of_orders
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1

SELECT 
  customer_number
FROM Orders
GROUP BY customer_number
HAVING COUNT(*) = (SELECT MAX(order_count) FROM (SELECT COUNT(*) AS order_count FROM Orders GROUP BY customer_number) AS counts)
