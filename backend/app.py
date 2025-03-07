from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Replace with your AQICN API token
API_TOKEN = "dd54d0ecebff369e45f9ff135004c150617233df"

@app.route('/')
def home():
    return "Welcome to the AQI API! Use /aqi/<city> to get air quality data."


@app.route('/aqi/<city>', methods=['GET'])
def get_aqi(city):
    url = f"https://api.waqi.info/feed/{city}/?token={API_TOKEN}"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)