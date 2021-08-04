from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from pandas import DataFrame
from os import environ


class DbHandler:
    def __init__(self):
        self.connection = self._make_connection()

    def _make_connection(self) -> Connection:

        engine = create_engine(
            "postgresql+psycopg2://{}:{}@{}/{}".format(
                environ["POSTGRES_USER"],
                environ["POSTGRES_PASSWORD"],
                environ["POSTGRES_ADDRES"],
                environ["POSTGRES_DATABASE"],
            )
        )

        return engine.connect()

    def insert_dataframe(self, data: DataFrame, table: str) -> None:
        data.to_sql(
            name=table,
            con=self.connection,
            if_exists="append",
            chunksize=5000,
            method="multi",
            index=False,
        )
