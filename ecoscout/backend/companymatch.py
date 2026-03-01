# companymatch.py is the test function we used before transferring the code over to funcs.py

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"C:\Users\espyc\Documents\GitHub\Eco-scout\ecoscout\backend\credentials.json")
firebase_admin.initialize_app(cred)

#app = firebase_admin.initialize_app()
db = firestore.client()

from urllib.parse import urlparse, parse_qs
#Get the documents
docs = db.collection("FastFashionData").stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")




# Getting brand name from URL

#Example URL
url = "https://www2.hm.com/en_us/index.html"

# Identifies the brand from url
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

# Brand
brand = get_brand_from_url(url)
print(f"URL Brand: {brand}")

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


brand = get_brand_from_url(url)
print(f"Extracted brand: {brand}")

# CALL THE FUNCTION HERE:
match = match_brand_to_company(brand)
company = get_company_from_doc(match)

if match:
    print(f"Success! Found: {company}")
else:
    print("No match found in database.")