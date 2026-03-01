import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
db=firestore.client()

#app = firebase_admin.initialize_app()
db = firestore.client()

from urllib.parse import urlparse, parse_qs

for d in db.collection("FastFashionData").stream():
    print(d.id)
#Get the documents
doc_id = "0pvbEsazeeKdOAya259c"
docs = db.collection("FastFashionData").document(doc_id)


def get_rec_names(docs):
    my_strings = []
    doc=docs.get()
    if doc.exists:
        data = doc.to_dict()
        rec_refs = data.get("Recs", [])

        for recID in rec_refs:
            recDoc= db.collection("Recs").document(recID).get()
            rec=recDoc.get()
            if rec.exists:
                rec_data = rec.to_dict()
                company_name = rec_data.get("Company")
                if company_name:
                    my_strings.append(company_name)
            else:
                print(f"Document {recID} not found!")
    else:
        print(f"Document{doc_id} not found!")
    


    for name in my_strings:
        print(name)    
    return my_strings


rec_names=get_rec_names(docs)