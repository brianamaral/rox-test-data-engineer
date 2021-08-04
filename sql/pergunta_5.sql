SELECT soh."SalesOrderID"
	,soh."OrderDate"
	,replace(soh."TotalDue", ',', '.')::FLOAT AS qtd
FROM "SalesOrderHeader" soh
WHERE replace(soh."TotalDue", ',', '.')::FLOAT > 1000
	AND (
		extract(year FROM soh."OrderDate"::DATE) = 2011
		AND extract(month FROM soh."OrderDate"::DATE) = 9
		)
ORDER BY replace(soh."TotalDue", ',', '.')::FLOAT DESC;