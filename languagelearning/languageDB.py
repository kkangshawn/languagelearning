from pymongo import MongoClient
import os
from enum import Enum

class Collections(str, Enum):
    GERMAN_PHRASES = "german_phrases"
    GERMAN_WORDS = "german_words"
    ENGLISH_PHRASES = "english_phrases"
    USERS = "users"
    
def get_db():
    CONNECTION_STRING = os.environ['MONGODB_URI']
    client = MongoClient(CONNECTION_STRING)
    try:
        client.admin.command('ping')
    except Exception as e:
        print("Failed to ping your deployment. Check connetion to MongoDB!")
        print(e)
    return client['LanguageDB']

def get_collection(collection_name):
    return get_db()[collection_name]
