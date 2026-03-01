# funcs.py collects all the functions needed to get information from Firestore

import firebase_admin
from firebase_admin import credentials, firestore
from urllib.parse import urlparse, parse_qs

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# This function isolates the brand from the URL
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


# If the brand name matches a company name in our database, we return the document ID
def match_brand_to_company(brand):
    docs = db.collection("FastFashionData").stream()
    for doc in docs:
        data = doc.to_dict()
        company_name = data.get("Company", "").lower()
        if brand in company_name:
            print("Matched brand:", brand, "to Company:", company_name)
            return doc.id # Return the document ID
    return None

# Each of these functions grabs a specific piece of information from the document
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

# Determines our "final rating" depending on the sustainability and ethicality rating.
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
    
# Returns an array of the recommended brands based on the document ID
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

# Returns an array of the recommended brands URLS based on the document ID
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