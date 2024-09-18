from azure.cosmos import exceptions, CosmosClient, PartitionKey
import json

#Initialize the Cosmos Client
endpoint = "xxxx"
key = "xxxxx"
DATABASE_NAME = "bank-azuredb"
CONTAINER_NAME = "customercontainer"

#create a cosmos client - Establish connection with Axure CosmosDB
client = CosmosClient(endpoint, key)

#select the database
database = client.get_database_client(DATABASE_NAME)

#select container name
container = database.get_container_client(CONTAINER_NAME)

query = "SELECT * FROM c"

try:
    items = container.query_items(
        query = query,
        enable_cross_partition_query = True 
    )
    lst = []
    for item in items:
        lst.append(item)


    with open("output.json", 'w') as file:
        json.dump(lst, file, indent=4)
    print(f"Data successfully written.")

    
except exceptions.CosmosHttpResponseError as e:
    print(f"An error occured {e.message}")


