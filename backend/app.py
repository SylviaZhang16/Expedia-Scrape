from flask import Flask, request, jsonify
import asyncio
from new_scrape import fetch_hotels  
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to Hotel Search API!"


@app.route('/search', methods=['POST'])
def search():
    data = request.json
    hotels = fetch_hotels(data['destination'], data['start_date'], data['end_date'])
    return jsonify(hotels)

if __name__ == '__main__':
    app.run(debug=True)