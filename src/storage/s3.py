from __future__ import annotations

from io import BytesIO, StringIO
from urllib.parse import urlparse

import boto3
import pandas as pd


def split_s3_uri(uri: str) -> tuple[str, str]:
    parsed = urlparse(uri)
    if parsed.scheme != "s3":
        raise ValueError(f"Expected s3:// URI, got: {uri}")
    return parsed.netloc, parsed.path.lstrip("/")


class S3StorageClient:
    def __init__(self, region_name: str | None = None):
        self.s3 = boto3.client("s3", region_name=region_name)

    def read_csv(self, uri: str) -> pd.DataFrame:
        bucket, key = split_s3_uri(uri)
        obj = self.s3.get_object(Bucket=bucket, Key=key)
        return pd.read_csv(obj["Body"])

    def write_parquet(self, df: pd.DataFrame, uri: str) -> None:
        bucket, key = split_s3_uri(uri)
        buffer = BytesIO()
        df.to_parquet(buffer, index=False)
        buffer.seek(0)
        self.s3.put_object(Bucket=bucket, Key=key, Body=buffer.getvalue())

    def write_json(self, data: str, uri: str) -> None:
        bucket, key = split_s3_uri(uri)
        self.s3.put_object(Bucket=bucket, Key=key, Body=data.encode("utf-8"))

    def exists(self, uri: str) -> bool:
        bucket, key = split_s3_uri(uri)
        try:
            self.s3.head_object(Bucket=bucket, Key=key)
            return True
        except self.s3.exceptions.ClientError:
            return False

    def list_keys(self, bucket: str, prefix: str) -> list[str]:
        paginator = self.s3.get_paginator("list_objects_v2")
        keys: list[str] = []

        for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
            for obj in page.get("Contents", []):
                keys.append(obj["Key"])
