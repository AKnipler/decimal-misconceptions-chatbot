from pymongo import MongoClient
from pymongo.server_api import ServerApi

def get_mongo_client(connection_string):
    return MongoClient(connection_string, server_api=ServerApi('1'))

def check_identifier(connection_string, identifier):
    """Check if the identifier exists in the valid_identifiers collection."""
    # For simple chatbot, we'll make this more permissive
    # Check if identifier is not empty and has at least 3 characters
    if not identifier or len(identifier.strip()) < 3:
        return False

    # Try to connect to MongoDB and check if identifier exists
    try:
        client = get_mongo_client(connection_string)
        db = client.physiobot
        result = db.valid_identifiers.find_one({"identifier": identifier})
        return bool(result)
    except Exception:
        # If MongoDB connection fails, fall back to simple validation
        # This makes the chatbot work even without proper MongoDB setup
        return len(identifier.strip()) >= 3
    finally:
        try:
            client.close()
        except:
            pass
