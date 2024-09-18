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



with open('customer.json', 'r') as file:
    data = json.load(file)


for item in data:
    try:
        container.upsert_item(item)
        print(f"Item with id {item['id']} upserted successfully.")
    except exceptions.CosmosHttpResponseError as e:
        print(f"An error occurred while upserting item with id {item['id']}: {e.message}")