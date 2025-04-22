from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:Test12345@edsa.0cvezxa.mongodb.net/?retryWrites=true&w=majority&appName=EDSA")

db = client.todo_db

collection_name = db["todo_collection"]