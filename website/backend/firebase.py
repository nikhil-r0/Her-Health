import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("healthapp-c5029-785648092a9b.json ")

firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()


# Fetch data from a specified document in Firestore
def fetch_data(collection):
    docs_ref = db.collection(collection)
    docs = docs_ref.stream()  # Fetch all documents in the collection
    data = []
    for doc in docs:
        data.append(doc.to_dict())  # Convert each document to a dictionary
    return data
