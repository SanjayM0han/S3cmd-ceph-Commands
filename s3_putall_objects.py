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
local_dir = './downloaded_files'  # Local directory containing files and folders to upload

try:
    bucket = s3.Bucket(bucket_name)

    # Upload all files and folders in the specified directory
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, local_dir)
            s3_key = relative_path.replace("\\", "/")  # Ensure correct path format for S3
            try:
                bucket.upload_file(local_path, s3_key)
                print(f"Uploaded {local_path} to {s3_key}")
            except ClientError as e:
                print(f"Failed to upload {local_path} to {s3_key}: {e}")

except NoCredentialsError:
    print("Error: No credentials provided")
except PartialCredentialsError:
    print("Error: Incomplete credentials provided")
except ClientError as e:
    print(f"Failed to process bucket '{bucket_name}': {e}")
