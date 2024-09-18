from azure.cosmos import exceptions, CosmosClient, PartitionKey
import json

#Initialize the Cosmos Client
endpoint = "xxx"
key = "xxxx"
DATABASE_NAME = "bank-azuredb"
CONTAINER_NAME = "customercontainer"

#create a cosmos client - Establish connection with Axure CosmosDB
client = CosmosClient(endpoint, key)

#select the database
database = client.get_database_client(DATABASE_NAME)

#select container name
container = database.get_container_client(CONTAINER_NAME)

print("\n1.Update\n2.Delete\n")
ch = input("Enter choice")

if ch == "1":

    print("\nEnter item to update\n")


    item_id = input("Enter item id: ")
    partition_key = input("Enter partition by: ")


    try:
       
        item = container.read_item(item_id,partition_key)
        
        item_name = input("Enter Customer name: ")
        item['name'] = item_name

        container.replace_item(item_id, item, partition_key)
        print(f"Item with id {item['id']} updated successfully.")

    except exceptions.CosmosResourceNotFoundError:
        print(f"Item with id {item_id} not found.")
    except exceptions.CosmosHttpResponseError as e:
        print(f"An error occurred while upserting item with id {item['id']}: {e.message}")


elif ch == '2':
    dummy_data = {
            "id": "ust100101",
            "name": "rohini",
            "product": "keyboard",
            "brand-name": "bose",
            "Country": "United Kingdom",
            "amount": 8000
        }

    try:

        container.upsert_item(dummy_data)

        print(f"Item dummy data inserted successfully.")
    except exceptions.CosmosHttpResponseError as e:
        print(f"An error occurred while upserting item {e.message}")


    print("\n Enter item to delete \n")

    item_id = input("Enter item id: ")
    partition_key = input("Enter partition by: ")

    try:
        container.delete_item(item_id, partition_key)
        print(f"Item with id {item_id} deleted successfully.")
    except exceptions.CosmosResourceNotFoundError:
        print(f"Item with id {item_id} not found.")
    except exceptions.CosmosHttpResponseError as e:
        print(f"An error occurred while deleting item {e.message}")