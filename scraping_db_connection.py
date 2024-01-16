import json
from pymongo import MongoClient

my_database_url = "mongodb+srv://traveler:********@cluster0.fssqv0f.mongodb.net/"
my_database_name = "homework9"
quotes_collection_name = "quotes"
authors_collection_name = "authors"


def upload_to_mongodb_atlas(database_url, database_name, collection_name, data):
    client = MongoClient(database_url)
    db = client[database_name]
    collection = db[collection_name]

    for item in data:
        collection.insert_one(item)


if __name__ == "__main__":
    with open('quotes.json', 'r') as quotes_file:
        quotes_data = json.load(quotes_file)

    with open('authors.json', 'r') as authors_file:
        authors_data = json.load(authors_file)

    upload_to_mongodb_atlas(my_database_url, my_database_name, quotes_collection_name, quotes_data)
    upload_to_mongodb_atlas(my_database_url, my_database_name, authors_collection_name, authors_data)
