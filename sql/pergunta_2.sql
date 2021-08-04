SELECT p."Name"
	,p."DaysToManufacture"
	,sum(sod."OrderQty") AS qtd
FROM "SalesOrderDetail" sod
LEFT JOIN "SpecialOfferProduct" sop ON sop."SpecialOfferID" = sod."SpecialOfferID"
LEFT JOIN "Product" p ON p."ProductID" = sop."ProductID"
GROUP BY p."Name"
	,p."DaysToManufacture"
ORDER BY 3 DESC limit 3;