import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

access_key = '40ONBHFED9HING9BQAVA'
secret_key = 'RsRgKDiODEF36RyNcUiRk8VjCXqtxzViYxx7Gvsh'

# Initialize a session using your access and secret key, and the endpoint URL
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='us-west-2'  # Replace with your region if needed
)

s3 = session.resource('s3', endpoint_url='http://ceph1:8000')

bucket_name = 'home'
local_dir = './Documents'  # Local directory to store downloaded files

# File to upload
file_to_upload = 'PutObject.java'
s3_key_for_upload = 'PutObject.java'  # The key under which the file will be stored in the bucket

# Create the local directory if it does not exist
if not os.path.exists(local_dir):
    os.makedirs(local_dir)

try:
    bucket = s3.Bucket(bucket_name)

    # Upload the 'bootstrap' file
    if os.path.exists(file_to_upload):
        bucket.upload_file(file_to_upload, s3_key_for_upload)
        print(f"Uploaded {file_to_upload} to {s3_key_for_upload}")
    else:
        print(f"File {file_to_upload} does not exist, skipping upload.")

except NoCredentialsError:
    print("Error: No credentials provided")
except PartialCredentialsError:
    print("Error: Incomplete credentials provided")
except ClientError as e:
    print(f"Failed to process bucket '{bucket_name}': {e}")