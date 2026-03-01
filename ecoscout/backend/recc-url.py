import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"C:\Users\faith\Documents\GitHub\Eco-scout\ecoscout\backend\credentials.json")
firebase_admin.initialize_app(cred)


#app = firebase_admin.initialize_app()
db = firestore.client()

from urllib.parse import urlparse, parse_qs

#Get the documents
doc_id = "0pvbEsazeeKdOAya259c"
docs = db.collection("FastFashionData").document(doc_id)


def get_rec_names(docs):
    my_strings = []
    doc=docs.get()
    if doc.exists:
        data = doc.to_dict()
        rec_refs = data.get("Recc", [])

        for recID in rec_refs:
            rec=recID.get()
            if rec.exists:
                rec_data = rec.to_dict()
                url = rec_data.get("URL")
                print(url)
                if url:
                    my_strings.append(url)
            else:
                print(f"Document {recID} not found!")
    else:
        print(f"Document{doc_id} not found!")



    return my_strings


    
rec_names=get_rec_names(docs)
 

