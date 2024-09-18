from dotenv import load_dotenv
import os
from azure.storage.blob import ContainerClient, BlobClient, BlobServiceClient

load_dotenv()

CONNECTION_STRING = os.getenv('CONNECTION_STRING')
ACCOUNT_KEY = os.getenv('ACCOUNT_KEY')
ACCOUNT_NAME = os.getenv('ACCOUNT_NAME')

connection_string = CONNECTION_STRING
account_key = ACCOUNT_KEY
account_name = ACCOUNT_NAME

blob_storage_client = BlobServiceClient.from_connection_string(connection_string)

blobclient = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net/", credential=account_key)

# Access container and list blobs
container_name = "azureblobcontainer"
container_client = blob_storage_client.get_container_client(container_name)


local_file_path = "C:/Users/Administrator/Downloads/transformed_sales_data.json"

with open(local_file_path,"rb") as obj:
    container_client.upload_blob("sales_data.json", obj)
    print("blob uploaded")

blob_list = container_client.list_blob_names()

for blobs in blob_list:
    print(blobs)
