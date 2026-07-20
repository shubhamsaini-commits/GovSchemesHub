import os
import sys
# pyrefly: ignore [missing-import]
# pyrefly: ignore [missing-import]
# pyrefly: ignore [missing-import]
from flask import Flask, jsonify, request
from flask_cors import CORS
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv, find_dotenv

# Load environment variables from the root .env file
load_dotenv(find_dotenv())

# Add KIBO to python system path for importing modules from it
current_dir = os.path.dirname(os.path.abspath(__file__))
kibo_dir = os.path.abspath(os.path.join(current_dir, "..", "KIBO"))
if kibo_dir not in sys.path:
    sys.path.append(kibo_dir)

# pyrefly: ignore [missing-import]
from rag import ask_with_rag

app = Flask(__name__)

# Configure CORS specifically for the frontend local dev environment
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

# Home route
@app.route("/")
def home():
    return "Backend is running 🚀"

# Test API
@app.route("/api/test")
def test():
    return jsonify({"message": "API working!"})

# Query RAG API
@app.route("/api/query", methods=["POST"])
def query_rag():
    data = request.get_json(silent=True) or {}
    question = data.get("question")
    
    if not question or not question.strip():
        return jsonify({"error": "Missing or empty 'question' in request body"}), 400
        
    try:
        answer = ask_with_rag(question)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": f"An error occurred during query execution: {str(e)}"}), 500

# Schemes API
@app.route("/api/schemes")
def schemes():
    return jsonify({
        "schemes": [
            {"name": "PM Kisan", "benefit": "₹6000/year"},
            {"name": "Ayushman Bharat", "benefit": "Health insurance"}
        ]
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)