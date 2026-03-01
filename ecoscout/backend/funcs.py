import firebase_admin
from firebase_admin import credentials, firestore
from urllib.parse import urlparse, parse_qs

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_brand_from_url(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    
    # Remove www if present
    if hostname.startswith("www."):
        hostname = hostname.replace("www.", "")
    
    # Split by dot
    parts = hostname.split(".")
    
    # If subdomain exists, grab main domain
    if len(parts) > 2:
        brand = parts[-2]
    else:
        brand = parts[0]
    
    return brand.lower()


# If brand name matches firebase company names
def match_brand_to_company(brand):
    docs = db.collection("FastFashionData").stream()
    for doc in docs:
        data = doc.to_dict()
        company_name = data.get("Company", "").lower()
        if brand in company_name:
            print("Matched brand:", brand, "to Company:", company_name)
            return doc.id # Return the document ID
    return None

def get_company_from_doc(doc_id):
    doc = db.collection("FastFashionData").document(doc_id).get()
    if doc.exists:
        return doc.to_dict().get("Company")
    return None

def get_name_from_doc(doc_id):
    doc = db.collection("FastFashionData").document(doc_id).get()
    if doc.exists:
        return doc.to_dict().get("Name")
    return None

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
    

def get_rec_names(document_id):
    my_strings = []
    doc = db.collection("FastFashionData").document(document_id).get()
    if doc.exists:
        data = doc.to_dict()
        rec_refs = data.get("Recc", [])

        for recID in rec_refs:
            #recDoc= db.collection("Recs").document(recID).get()
            rec=recID.get()
            if rec.exists:
                rec_data = rec.to_dict()
                company_name = rec_data.get("Company")
                print(company_name)
                if company_name:
                    my_strings.append(company_name)
            else:
                print(f"Document {recID} not found!")
    else:
        print(f"Document {document_id} not found!")

    return my_strings


def get_rec_urls(document_id):
    my_strings = []
    doc = db.collection("FastFashionData").document(document_id).get()
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
        print(f"Document {document_id} not found!")

    return my_strings