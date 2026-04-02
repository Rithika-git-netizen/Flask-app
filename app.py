from flask import Flask, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"

# Route 1: Get Posts
@app.route("/posts", methods=["GET"])
def get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    return jsonify(response.json())

# Route 2: Get Comments
@app.route("/comments", methods=["GET"])
def get_comments():
    response = requests.get(f"{BASE_URL}/comments")
    return jsonify(response.json())


@app.route("/albums", methods=["GET"])
def get_albums():
    response = requests.get(f"{BASE_URL}/albums")
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True) 