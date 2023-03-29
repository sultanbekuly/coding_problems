/* Write your T-SQL query statement below */
SELECT 
s.stock_name
,SUM(s.[sum]) AS capital_gain_loss 
FROM
  (SELECT
  stock_name, operation
  ,CASE 
    WHEN operation='Buy' THEN SUM(price)*-1
    ELSE SUM(price) END AS [sum]
  FROM Stocks 
  GROUP BY stock_name, operation) s
GROUP BY s.stock_name