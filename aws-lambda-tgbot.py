import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    # try:
    #     response = s3_client.upload_file(file_name, bucket, object_name)
    # except ClientError as e:
    #     logging.error(e)
    #     return False
    # return True

    with open("file", "rb") as f:
        f.write = "newtest"
        s3.upload_fileobj(f, "vedro-0", "test-lambda1.txt")
