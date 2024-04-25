from quart import Quart, request, jsonify
import asyncio
from new_scrape import fetch_hotels 
from quart_cors import cors

app = Quart(__name__)
app = cors(app) 



@app.route('/')
async def home():
    return "Welcome to Hotel Search API!"

@app.route('/search', methods=['POST'])
async def search():
    data = await request.get_json()
    hotels = await fetch_hotels(data['destination'], data['start_date'], data['end_date'])
    return jsonify(hotels)

if __name__ == '__main__':
    app.run(debug=True)
