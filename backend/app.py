from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from the frontend

@app.route("/generate-music", methods=["POST"])
def generate_music():
    data = request.json
    # Placeholder logic for music generation
    return jsonify({"message": "Music generated successfully", "data": data})

if __name__ == "__main__":
    app.run(debug=True)