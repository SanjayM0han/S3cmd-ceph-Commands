import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

access_key = '40ONBHFED9HING9BQAVA'
secret_key = 'RsRgKDiODEF36RyNcUiRk8VjCXqtxzViYxx7Gvsh'

# Initialize a session using your access and secret key, and the endpoint URL
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
   # region_name='us-west-2'  # Replace with your region if needed
)

s3 = session.resource('s3', endpoint_url='http://ceph1:8000')

bucket_name = 'test'
local_dir = './downloaded_files'  # Local directory to store downloaded files

# Create the local directory if it does not exist
if not os.path.exists(local_dir):
    os.makedirs(local_dir)

try:
    bucket = s3.Bucket(bucket_name)
    print(f"Downloading contents of bucket '{bucket_name}':")
    for obj in bucket.objects.all():
        local_path = os.path.join(local_dir, obj.key)
        if not os.path.exists(os.path.dirname(local_path)):
            os.makedirs(os.path.dirname(local_path))
        bucket.download_file(obj.key, local_path)
        print(f"- {obj.key} downloaded to {local_path}")
except NoCredentialsError:
    print("Error: No credentials provided")
except PartialCredentialsError:
    print("Error: Incomplete credentials provided")
except ClientError as e:
    print(f"Failed to download contents of bucket '{bucket_name}': {e}")