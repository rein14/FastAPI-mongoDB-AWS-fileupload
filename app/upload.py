import os
from dataclasses import asdict, dataclass
from typing import Optional, Union

import aiofiles
import boto3
from botocore.exceptions import ClientError
from core.config import Settings
import logging

LOGGER = logging.getLogger(__name__)


@dataclass
class AwsConnection:
    aws_access_key_id: Optional[str]
    aws_secret_key: Optional[str]
    region_name: Optional[str]


def get_aws_creds() -> AwsConnection:
    """get AWS credentials"""
    return AwsConnection(
        aws_access_key_id=Settings.AWS_ACCESS_ID,
        aws_secret_key=Settings.AWS_ACCESS_KEY,
        region_name=Settings.AWS_REGION,
    )


def get_client():
    """get s3 client"""
    s3 = boto3.client("s3", **asdict(get_aws_creds()))
    return s3


async def handle_file_upload(files) -> bool:
    """handle file upload
    params: files
    return: Bool"""
    client = get_client()
    aws_bucket_name = Settings.BUCKET_NAME

    for file in files:
        try:
            async with aiofiles.open(file.file, "rb") as data:
                client.upload_fileobj(data, aws_bucket_name, file.filename)
        except ClientError as e:
            LOGGER.info("Failed to upload file")
            LOGGER.error(e)
            return False
    LOGGER.info("Files uploaded")
    return True


async def fileUrl(handler):
    "url for upload image "
    url = f"https://{handler.aws_bucket_name}s3.{Settings.AWS_REGION}.amazonaws.com/{handler.filePath}"
    if handler:
        return url
    else:
        url = "files not uploaded"
        return url
