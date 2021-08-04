from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from pandas import DataFrame

class DbHandler:
    def __init__(self):
        self.connection = self._make_connection()
    
    def _make_connection(self) -> Connection:
        
        engine = create_engine("postgresql+psycopg2://postgres:rox-partner@database-1.clc0z9jsa3ep.us-east-1.rds.amazonaws.com/postgres")
    
        return engine.connect()
    
    def insert_dataframe(self,data: DataFrame,table: str) -> None:
        data.to_sql(name=table,con=self.connection,if_exists='append',chunksize=5000,method='multi',index=False)
        
        
        