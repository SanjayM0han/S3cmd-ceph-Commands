import boto3
from botocore.exceptions import ClientError

access_key = '40ONBHFED9HING9BQAVA'
secret_key = 'RsRgKDiODEF36RyNcUiRk8VjCXqtxzViYxx7Gvsh'

# Initialize a session using your access and secret key, and the endpoint URL
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='us-west-2'  # Replace with your region if needed
)

s3 = session.resource('s3', endpoint_url='http://ceph1:8000')

# List existing buckets
try:
    for bucket in s3.buckets.all():
        print(f"Bucket: {bucket.name}")
except ClientError as e:
    print(f"Failed to list buckets: {e}")

# Create a new bucket
bucket_name = 'my-new-bucket'
try:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created successfully")
except ClientError as e:
    print(f"Failed to create bucket: {e}")
