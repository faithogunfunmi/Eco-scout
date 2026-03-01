from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS, cross_origin
import funcs


app = Flask(__name__, static_folder="../../frontend/crud_app/dist", static_url_path="/")
CORS(app,
     resources={r"/*": {"origins": "chrome-extension://dcmfcppjhgfgachphnifcijnnjihgjkb"}},
     allow_headers=["Content-Type", "Authorization"],
     methods=["GET", "POST", "OPTIONS"],
     supports_credentials=True)


@app.route("/", methods=["GET"])
def test():
    return jsonify({"message": "Backend is running!"})

@app.route("/", methods=["POST"])
def get_data():
    print("Received POST request with data:", request.json.get("url"))
    url = request.json.get("url")

    if not url:
        return jsonify({"error": "URL not found"}), 400

    brand = funcs.get_brand_from_url(url)
    docId = funcs.match_brand_to_company(brand)
    company = funcs.get_name_from_doc(docId)

    reccomendations = funcs.get_rec_names(docId)
    reccomendURL = funcs.get_rec_urls(docId)

     # can fix this later such that it reccomends the best 3 sustainable brands
    if(reccomendations == None or len(reccomendations) == 0):
        reccomendations = ["No recommendations found"]
    if(reccomendURL == None or len(reccomendURL) == 0):
        reccomendURL = ["google.com"]


    return jsonify({
        "name": company,
        "sustainability": funcs.get_sustain_rating(docId),
        "ethics": funcs.get_ethic_rating(docId),
        "overall": funcs.get_total_rating(docId),
        "recommendations": reccomendations, # THIS CAN NEVER BE EMPTY OR THERE WILL BE AN ERROR
        "recommendURL": reccomendURL # THIS CAN NEVER BE EMPTY OR THERE WILL BE AN ERROR
        }), 200

if __name__ == "__main__":
    app.run(port=8080,debug=True,host="0.0.0.0")