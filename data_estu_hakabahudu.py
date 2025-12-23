# %%
from pathlib import Path

# Path of the folder you want to create
folder_path = Path("tmp/bomma")

# Create the folder (creates parent folders if needed)
folder_path.mkdir(parents=True, exist_ok=True)

print("Folder 'tmp/bomma' created successfully")


# %%
import os
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError

# 🔐 Read secrets from environment variables
ACCOUNT_ID = os.environ["R2_ACCOUNT_ID"]
ACCESS_KEY_ID = os.environ["R2_ACCESS_KEY"]
SECRET_ACCESS_KEY = os.environ["R2_SECRET_KEY"]
BUCKET = os.environ["R2_BUCKET"]

# Create S3 client for Cloudflare R2
s3 = boto3.client(
    "s3",
    endpoint_url=f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com",
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    region_name="auto",
    config=Config(
        signature_version="s3v4",
        s3={"addressing_style": "virtual"}
    )
)

# File paths
remote_key = "Desktop/1.zip"
local_path = "tmp/bomma/1.zip"

print("Downloading... please wait")

try:
    s3.download_file(BUCKET, remote_key, local_path)
    print("✅ Download completed successfully!")
except ClientError as e:
    print("❌ Download failed:", e)


# %%
import os
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError

# 🔐 Read secrets from environment variables
ACCOUNT_ID = os.environ["R2_ACCOUNT_ID"]
ACCESS_KEY_ID = os.environ["R2_ACCESS_KEY"]
SECRET_ACCESS_KEY = os.environ["R2_SECRET_KEY"]
BUCKET = os.environ["R2_BUCKET"]

# Create S3 client for Cloudflare R2
s3 = boto3.client(
    "s3",
    endpoint_url=f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com",
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    region_name="auto",
    config=Config(
        signature_version="s3v4",
        s3={"addressing_style": "virtual"}
    )
)

# File paths
remote_key = "Desktop/2.zip"
local_path = "tmp/bomma/2.zip"

print("Downloading... please wait")

try:
    s3.download_file(BUCKET, remote_key, local_path)
    print("✅ Download completed successfully!")
except ClientError as e:
    print("❌ Download failed:", e)


# %%
import os
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError

# 🔐 Read secrets from environment variables
ACCOUNT_ID = os.environ["R2_ACCOUNT_ID"]
ACCESS_KEY_ID = os.environ["R2_ACCESS_KEY"]
SECRET_ACCESS_KEY = os.environ["R2_SECRET_KEY"]
BUCKET = os.environ["R2_BUCKET"]

# Create S3 client for Cloudflare R2
s3 = boto3.client(
    "s3",
    endpoint_url=f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com",
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    region_name="auto",
    config=Config(
        signature_version="s3v4",
        s3={"addressing_style": "virtual"}
    )
)

# File paths
remote_key = "Desktop/3.zip"
local_path = "tmp/bomma/3.zip"

print("Downloading... please wait")

try:
    s3.download_file(BUCKET, remote_key, local_path)
    print("✅ Download completed successfully!")
except ClientError as e:
    print("❌ Download failed:", e)


# %%
import os
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError

# 🔐 Read secrets from environment variables
ACCOUNT_ID = os.environ["R2_ACCOUNT_ID"]
ACCESS_KEY_ID = os.environ["R2_ACCESS_KEY"]
SECRET_ACCESS_KEY = os.environ["R2_SECRET_KEY"]
BUCKET = os.environ["R2_BUCKET"]

# Create S3 client for Cloudflare R2
s3 = boto3.client(
    "s3",
    endpoint_url=f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com",
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    region_name="auto",
    config=Config(
        signature_version="s3v4",
        s3={"addressing_style": "virtual"}
    )
)

# File paths
remote_key = "Desktop/4.zip"
local_path = "tmp/bomma/4.zip"

print("Downloading... please wait")

try:
    s3.download_file(BUCKET, remote_key, local_path)
    print("✅ Download completed successfully!")
except ClientError as e:
    print("❌ Download failed:", e)


# %%
import os
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError

# 🔐 Read secrets from environment variables
ACCOUNT_ID = os.environ["R2_ACCOUNT_ID"]
ACCESS_KEY_ID = os.environ["R2_ACCESS_KEY"]
SECRET_ACCESS_KEY = os.environ["R2_SECRET_KEY"]
BUCKET = os.environ["R2_BUCKET"]

# Create S3 client for Cloudflare R2
s3 = boto3.client(
    "s3",
    endpoint_url=f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com",
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    region_name="auto",
    config=Config(
        signature_version="s3v4",
        s3={"addressing_style": "virtual"}
    )
)

# File paths
remote_key = "Desktop/5.zip"
local_path = "tmp/bomma/5.zip"

print("Downloading... please wait")

try:
    s3.download_file(BUCKET, remote_key, local_path)
    print("✅ Download completed successfully!")
except ClientError as e:
    print("❌ Download failed:", e)



