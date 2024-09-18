from azure.cosmos import exceptions, CosmosClient, PartitionKey
import json

#Initialize the Cosmos Client
endpoint = "xxx"
key = "xxxx"
DATABASE_NAME = "bank-azuredb"
CONTAINER_NAME = "bankcontainer"

#create a cosmos client - Establish connection with Axure CosmosDB
client = CosmosClient(endpoint, key)

#select the database
database = client.get_database_client(DATABASE_NAME)

#select container name
container = database.get_container_client(CONTAINER_NAME)

query = "SELECT * FROM c"
count = 0
try:
    items = container.query_items(
        query = query,
        enable_cross_partition_query = True 
    )
    for item in items:
        count+=1
        print(item)

    
except exceptions.CosmosHttpResponseError as e:
    print(f"An error occured {e.message}")

print(count)

