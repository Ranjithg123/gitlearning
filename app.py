from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Dummy weather data
weather_data = {
    "Chennai": {"temperature": 34, "condition": "Sunny"},
    "Mumbai": {"temperature": 30, "condition": "Humid"},
    "Delhi": {"temperature": 38, "condition": "Hot"},
    "Bangalore": {"temperature": 28, "condition": "Cloudy"}
}

# Home
@app.route('/')
def home():
    return render_template("index.html")

# Get weather for all cities
@app.route('/weather', methods=['GET'])
def get_all_weather():
    return jsonify(weather_data)

# Get weather by city name
@app.route('/weather/<city>', methods=['GET'])
def get_weather_by_city(city):
    city = city.capitalize()
    if city in weather_data:
        return jsonify({city: weather_data[city]})
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
