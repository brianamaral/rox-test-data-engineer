from handler import DbHandler
from data_getter import DataGetter

data_getter = DataGetter()

handler = DbHandler()

files_and_tables = [
    {"table": "SalesOrderDetail", "file": "sales/Sales.SalesOrderDetail.csv"},
    {"table": "SalesOrderHeader", "file": "sales/Sales.SalesOrderHeader.csv"},
    {"table": "Person", "file": "person/Person.Person.csv"},
    {"table": "SpecialOfferProduct", "file": "sales/Sales.SpecialOfferProduct.csv"},
    {"table": "Customer", "file": "sales/Sales.Customer.csv"},
    {"table": "Product", "file": "production/Production.Product.csv"},
]


def lambda_handler(event, context):

    for pair in files_and_tables:
        data = data_getter.create_data_frame(file=pair["file"])
        handler.insert_dataframe(table=pair["table"], data=data)
        del data

    return "sucess"
