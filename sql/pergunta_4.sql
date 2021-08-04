select
sod."ProductID"
,soh."OrderDate"
,sum(sod."OrderQty") as qtd
from "SalesOrderHeader" soh 
join "SalesOrderDetail" sod on soh."SalesOrderID" = sod."SalesOrderID"
group by sod."ProductID",
		 soh."OrderDate"
order by 3 desc;