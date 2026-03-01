import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"C:\\Users\\faith\\Documents\\GitHub\\Eco-scout\\ecoscout\\backend\\credentials.json")
firebase_admin.initialize_app(cred)

#app = firebase_admin.initialize_app()
db = firestore.client()

from urllib.parse import urlparse, parse_qs

# Example document ID from FastFashionData collection
doc_id = "0pvbEsazeeKdOAya259c"
docs = db.collection("FastFashionData").document(doc_id)

recID_arr = []


def get_rec_names(docs):
    counter = 0
    my_strings = []
    doc=docs.get()
    if doc.exists:
        data = doc.to_dict()
        rec_refs = data.get("Recc", [])
        for recID in rec_refs:
            recDoc= db.collection("Recc").document(recID.id)
            rec=recDoc.get()
            if rec.exists:
                print("Rec exists")
                rec_data = rec.to_dict()
                company_name = rec_data.get("Company")
                if company_name:
                    my_strings.append(company_name)
            else:
                print(f"Document IDs: {recID.id}!")
                my_strings.append(recID.id)
    else:
        print(f"Document {doc_id} not found!")
            

    for name in my_strings:
        print(name)    
    return my_strings


#Get Recs
docs_recs = db.collection("Recs").document(doc_id)
for names in docs:
    print(f"{names.id} => {names.to_dict()}")

for names in docs:
        data = names.to_dict()
        urls = data.get("URL", "").lower()
        if names in urls:
            print("Matched brand:", names, "to URL:", urls)
            #return names.id # Return the document ID
    #return None

# if my_strings in company_name:
#             print("Matched brand:", brand, "to Company:", company_name)
#             return doc.id # Return the document ID


rec_names=get_rec_names(docs)
print(rec_names)


# # 1. Initialize an empty array to store the rec-ids
# rec_id_list = []
# doc_id = "0pvbEsazeeKdOAya259c"

# def get_info_from_doc_id(doc_id):
#     doc_ref = db.collection("FastFashionData").document(doc_id)
#     doc = doc_ref.get()
    
#     if doc.exists:
#         data = doc.to_dict()
        
#         # 1. Get the Company Name (This is a String)
#         company_name = data.get("Company")
#         print(f"Company Name: {company_name}")
        
#         # 2. Get the Recc section (This is a separate field from Company)
#         # We look inside 'data' again, NOT inside 'company_name'
#         recc_section = data.get("Recc", []) 
        
#         # Determine the initial rec_id (which currently is a Reference object)
#         if isinstance(recc_section, list):
#             rec_id = recc_section[0] if len(recc_section) > 0 else None
#         elif isinstance(recc_section, dict):
#             rec_id = recc_section.get("Recc")
#         else:
#             rec_id = recc_section

#         # --- DEREFERENCING LOGIC ---
#         if isinstance(rec_id, list):
#             # Option A: If you just want the ID string of the linked doc:
#             final_rec_id = rec_id
            
#             # Option B: If you want to see the actual URL/Data inside that linked doc:
#             # linked_doc = raw_val.get()
#             # final_rec_id = linked_doc.to_dict().get("url_field_name")
#         else:
#             final_rec_id = rec_id
#         # # 3. Handle if Recc is a List or a Map
#         # if isinstance(recc_section, list):
#         #     rec_id = recc_section[0] if len(recc_section) > 0 else None
#         # elif isinstance(recc_section, dict):
#         #     # If it's a map/dictionary, we get the nested 'Recc' key
#         #     rec_id = recc_section.get("Recc")
#         # else:
#         #     # If Recc is just a plain string in the DB
#         #     rec_id = recc_section

#         print(f"Company Name: {company_name}")
#         print(f"Rec-id: {final_rec_id}")

#         if rec_id:
#             rec_id_list.append(rec_id)
            
#         return rec_id_list
#     else:
#         print("Document not found!")
#         return None, None
    

# # Call the function for a specific document ID
# print("\n--- Final Rec ID List ---")
# print(rec_id_list)
# #return get_info_from_doc_id(doc_id)



# #Get the documents
# docs = db.collection("FastFashionData").stream()


# # 1. Initialize an empty list (array) to store the rec-ids
# rec_id_list = []

# doc_id = "0pvbEsazeeKdOAya259c"

# def get_info_from_doc_id(doc_id):
#     doc_ref = db.collection("FastFashionData").document(doc_id)
#     doc = doc_ref.get()
    
#     if doc.exists:
#         data = doc.to_dict()
        
#         # 1. Get the Company Name
#         company_name = data.get("Company")
        
#         # 2. Get the URL (Accessing the nested RECC map)
#         # We use .get("RECC", {}) to avoid errors if the map is missing
#         recc_section = data.get("Company").get("Recc", {})
#         if isinstance(recc_section, list):
#             # If it's a list, we can't use .get(). 
#             # We either take the first item or the whole list.
#             rec_id = recc_section[0] if len(recc_section) > 0 else None
#         else:
#             rec_id = recc_section.get("Recc", []) # This grabs the actual URL string
        
#         print(f"Company Name: {company_name}")
#         print(f"Rec-id: {rec_id}")

#         # 5. Add the rec_id to our array if it exists
#         if rec_id:
#             rec_id_list.append(rec_id)
        
#         #return company_name, rec_id
#     else:
#         print("Document not found!")
#         return None, None

# # Run the function
# get_info_from_doc_id(doc_id)

# # 6. Check your final array
# print("\n--- All Stored Rec-IDs ---")
# print(rec_id_list)

# # # Call the function
# # get_info_from_doc_id(doc_id)





