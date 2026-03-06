from pymongo import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st
from datetime import datetime

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
        db = client.decmisbot
        result = db.valid_identifiers.find_one({"identifier": identifier})
        return bool(result)
    except Exception:
        # If MongoDB connection fails, fall back to simple validation
        # This makes the chatbot work even without proper MongoDB setup
        return False # len(identifier.strip()) >= 3
    finally:
        try:
            client.close()
        except:
            pass


def log_transcript(connection_string, conversation_type, messages):
    client = get_mongo_client(connection_string)
    db = client.decmisbot
    collection = db.transcripts

    try:
        # Create new document for previous conversation
        document = {
            "timestamp": datetime.utcnow(),
            "messages": messages,
            "identifier": st.session_state.get("user_identifier", "anonymous")
        }
        result = collection.insert_one(document)
        return str(result.inserted_id)
        
    finally:
        client.close()
