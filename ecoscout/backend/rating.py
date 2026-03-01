import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"C:\Users\espyc\Documents\GitHub\Eco-scout\ecoscout\backend\credentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def get_sustain_rating(document_id):
    doc = db.collection("FastFashionData").document(document_id).get()
    return doc.to_dict().get("Sustain")
    
def get_ethic_rating(document_id):
    doc = db.collection("FastFashionData").document(document_id).get()
    return doc.to_dict().get("Ethic")


def get_total_rating(document_id):
    doc = db.collection("FastFashionData").document(document_id).get()
    sustainRate = doc.to_dict().get("Sustain")
    ethicRate = doc.to_dict().get("Ethic")

    if sustainRate == 0 and ethicRate == 0:
        return 0
    elif sustainRate == 1 or ethicRate == 1:
        return 1
    else:
        return 2

docs = db.collection("FastFashionData").stream()
for doc in docs:
    doc = db.collection("FastFashionData").document(doc.id).get()
    print(doc.to_dict().get("Company") + ": ")
    print("Sustainability: " + str(get_sustain_rating(doc.id)))
    print("Ethics: " + str(get_ethic_rating(doc.id)))
    print("Total: " + str(get_total_rating(doc.id)))
    print()
    