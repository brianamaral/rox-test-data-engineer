WITH cte_sales
AS (
	SELECT sod."SalesOrderID"
		,count(sod."SalesOrderDetailID") AS qtd_linhas
	FROM "SalesOrderDetail" sod
	GROUP BY sod."SalesOrderID"
	)
	
SELECT *
FROM cte_sales
WHERE qtd_linhas >= 3;