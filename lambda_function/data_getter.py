import boto3
from boto3.s3.transfer import TransferConfig
from pandas import read_csv, DataFrame
from io import BytesIO
import os


class DataGetter:
    def __init__(self):
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=os.environ["aws_key"],
            aws_secret_access_key=os.environ["aws_secret"],
        )
        self.config = TransferConfig(max_concurrency=2)

    def create_data_frame(self, file: str) -> DataFrame:
        data = self._download_file_s3(file)

        return read_csv(data, sep=";")

    def _download_file_s3(self, file: str) -> BytesIO:
        fileobj = BytesIO()
        s3_file = self.s3.download_fileobj(
            "bucket-rox-raw", file, fileobj, Config=self.config
        )
        fileobj.seek(0)

        return fileobj
