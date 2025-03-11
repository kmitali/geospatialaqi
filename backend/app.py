from flask import Flask, send_from_directory
import requests

app = Flask(__name__)

# Serve QGIS-processed GeoJSON data
@app.route('/aqi-data', methods=['GET'])
def get_aqi_data():
    return send_from_directory('data', 'aqi_heatmap.geojson')

# Fetch real-time AQI data
@app.route('/aqi/<city>', methods=['GET'])
def get_aqi(city):
    API_TOKEN = "dd54d0ecebff369e45f9ff135004c150617233df"
    url = f"https://api.waqi.info/feed/{city}/?token={API_TOKEN}"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)