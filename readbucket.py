"""Module dqwed."""
import logging
import boto3
from botocore.exceptions import ClientError

def enable_s3_bucket_logging():
    """Module dqwed."""
    aws_access_key_id = ''
    aws_secret_access_key = ''

    # Create an S3 client
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    try:
        # List all S3 buckets
        response = s3_client.get_object(Bucket='cdk-hnb659fds-assets-554142693511-ap-southeast-2', Key='02f325bea12ebe6009d08a5626a9f3dbfcaf1eae96a1c1f44d4c64bb155d9c68.zip')

        print(response)
        

    except ClientError as e:
        logging.error(e)

if __name__ == "__main__":
    enable_s3_bucket_logging()
