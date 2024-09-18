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

# list all blobs in the container
container_client = blob_storage_client.get_container_client(container_name)

blob_list = container_client.list_blob_names()

for blobs in blob_list:
    print(blobs)

#create a container if it doesn;t exist
def create_container(container_name):
    container_client = blob_storage_client.get_container_client(container_name)
    try:
        container_client.create_container()
        print(f"{container_name} Created")
    except Exception as e:
        print(f"Container creation failed {e}")

#upload
def upload_blob(container_name, blob_name, data):
    blob_client = blobclient.get_blob_client(container=container_name, blob=blob_name)
    try:
        blob_client.upload_blob(data=data, overwrite = True)
        print("Blob created and data uploaded to blob")
    except Exception as e:
        print("upload failed")

#delete
def delete_blob(container_name, blob_name):
    blob_client = blobclient.get_blob_client(container=container_name, blob=blob_name)
    try:
        blob_client.delete_blob()
        print(f"{blob_name} deleted")
    except Exception as e:
        print(f"Blob deletion failed {e}")

#download blob
def download_blob(container_name, blob_name, download_file_path):
    blob_client = blobclient.get_blob_client(container=container_name, blob=blob_name)
    try:
        with open(download_file_path, "wb") as obj:
            obj.write(blob_client.download_blob().readall())
            print("Download completed")
    except Exception as e:
        print(f"Download failed as {e}")


if __name__ == "__main__":
    create_container("azurepythoncontainer")
    # upload_blob("azurepythoncontainer", "blobfile.txt", "This is an example of blob upload")
    download_blob("azurepythoncontainer", "blobfile.txt","C:/Users/Administrator/Downloads/output.txt")
    # delete_blob("azurepythoncontainer", "blobfile.txt")