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
        response = s3_client.list_buckets()
        buckets = response['Buckets']

        if not buckets:
            print("No buckets found.")
            return

        print("S3 Buckets:")

        for bucket in buckets:
            if bucket['Name'] != "jamie-access-logs-target":
                try:
                    # Enable access logging for the specified S3 bucket
                    response = s3_client.put_bucket_logging(
                        Bucket=bucket['Name'],
                        BucketLoggingStatus={
                            'LoggingEnabled': {
                                'TargetBucket': "jamie-access-logs-target",
                                'TargetPrefix': bucket['Name'] + '/'
                            }
                        }
                    )
                    print(f"Access logging enabled for {bucket['Name']}.")

                except ClientError as e:
                    logging.error(e)

    except ClientError as e:
        logging.error(e)

if __name__ == "__main__":
    enable_s3_bucket_logging()
