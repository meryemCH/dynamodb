import os
import boto3
import pandas as pd
import sys

if sys.version_info[0] < 3:
    from StringIO import StringIO # Python 2.x
else:
    from io import StringIO # Python 3.x

# get your credentials from environment variables
aws_id = os.environ['Meryem@2020']
aws_secret = os.environ['V2j/zDF6VEDrARbOmMjsTMRwC3BkPI64nNvF0j9c']

client = boto3.client('s3', aws_access_key_id=aws_id,
        aws_secret_access_key=aws_secret)

bucket_name = 'meryembucket'

object_key = '2016_sample.csv'
csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
body = csv_obj['Body']
csv_string = body.read().decode('utf-8')

df = pd.read_csv(StringIO(csv_string))