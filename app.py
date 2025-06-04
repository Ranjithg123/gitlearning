from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Dummy weather data
weather_data = {
    "Chennai": {"temperature": 32, "condition": "Sunny", "lat": 13.0827, "lon": 80.2707},
    "Coimbatore": {"temperature": 30, "condition": "Cloudy", "lat": 11.0168, "lon": 76.9558},
    "Bangalore": {"temperature": 28, "condition": "Rainy", "lat": 12.9716, "lon": 77.5946},
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
    
@app.route('/weather/<city>')
def city_weather(city):
    city_title = city.title()
    if city_title in weather_data:
        return jsonify({city_title: weather_data[city_title]})
    else:
        return jsonify({"error": "City not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
