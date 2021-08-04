SELECT CONCAT (
		p."FirstName"
		,' '
		,p."MiddleName"
		,' '
		,p."LastName"
		) AS name
	,count(soh."SalesOrderID") AS qtd_compras
FROM "Person" p
JOIN "Customer" c ON c."PersonID" = p."BusinessEntityID"
JOIN "SalesOrderHeader" soh ON soh."CustomerID" = c."CustomerID"
GROUP BY 1
ORDER BY 2 DESC;