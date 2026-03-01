from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import funcs

app = Flask(__name__, static_folder="../../frontend/crud_app/dist", static_url_path="/")
CORS(app)

# Testing URL
testUrl = "https://www2.hm.com/en_us/index.html"

@app.route("/", methods=["POST"])
def get_data():
    data = request.json.get()
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL not found"}), 400

    brand = funcs.get_brand_from_url(url)
    docId = funcs.match_brand_to_company(brand)
    company = funcs.get_company_from_doc(docId)

    return jsonify({
        "name": company,
        "sustainability": funcs.get_sustain_rating(docId),
        "ethics": funcs.get_ethic_rating(docId),
        "overall": funcs.get_total_rating(docId),
        "reccomendations": []
        }), 200

if __name__ == "__main__":
    app.run(port=8080,debug=True)