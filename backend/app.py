from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash-001")

@app.route("/", methods=["GET"])
def home():
    return "Flask is working!"

@app.route("/chat", methods=["POST"])
def chat():
    print("Received request!")
    data = request.get_json()
    description = data.get("description", "")
    print("Description received:", description)
    response = model.generate_content(f"Return a hilarious and light-hearted joke about: {description}")
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
