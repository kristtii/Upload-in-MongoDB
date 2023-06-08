import json
from pymongo import MongoClient

# MongoDB cluster connection string
cluster_connection_string = "YOUR_SERVER"

# Path to the JSON file
json_file_path = 'test.json'

# Read the JSON file
with open(json_file_path, 'r') as file:
    json_data = json.load(file)

# Extract the field names and data
fields = json_data['data'][0]
data = json_data['data'][1:]

# Establish a connection to MongoDB cluster
cluster = MongoClient(cluster_connection_string)

# Access the target database and collection
db = cluster['DB_NAME']
collection = db['COLLECTION_NAME']

# Insert each data point as a separate document
for data_point in data:
    document = {}
    for key, value in zip(fields.keys(), data_point.values()):
        document[key] = value
    collection.insert_one(document)

print("JSON data uploaded to MongoDB cluster successfully!")
