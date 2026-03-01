import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"C:\\Users\\faith\\Documents\\GitHub\\Eco-scout\\ecoscout\\backend\\credentials.json")
firebase_admin.initialize_app(cred)

#app = firebase_admin.initialize_app()
db = firestore.client()

from urllib.parse import urlparse, parse_qs

#Get the documents
docs = db.collection("FastFashionData").stream()

doc_id = "0pvbEsazeeKdOAya259c"

def get_url_from_doc_id(document_id):
    doc = db.collection("FastFashionData").document(document_id).get()
    url = doc.to_dict().get("RECC").get("RECC")
    print(url)
    return url



