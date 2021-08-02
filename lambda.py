import boto3
import pandas as pd
import io
s3 = boto3.resource('s3',
           aws_access_key_id = '',
           aws_secret_access_key = '')

response = s3.Object(bucket_name='bucket-rox-raw',key='production/Production.Product.csv').get()

file = response['Body'].read()

pd.read_csv(io.BytesIO(file),sep=';')

