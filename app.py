import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

API_KEY = 'cb65223b85433968903b8215e7023d48'


def fetch_weather(city_name):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException:
        return None, 'Unable to reach weather service. Please try again.'

    if str(data.get('cod')) != '200':
        return None, data.get('message', 'Could not fetch weather for this city.')

    main = data.get('main', {})
    weather_list = data.get('weather', [{}])
    wind = data.get('wind', {})
    visibility_m = data.get('visibility', 0)

    weather = {
        'city': data.get('name', city_name),
        'temperature': round(main.get('temp', 0)),
        'feels_like': round(main.get('feels_like', main.get('temp', 0))),
        'description': weather_list[0].get('description', 'N/A').title(),
        'humidity': main.get('humidity', 0),
        'wind_speed': round(wind.get('speed', 0) * 3.6, 1),
        'visibility': round(visibility_m / 1000, 1),
        'pressure': main.get('pressure', 0)
    }

    return weather, None


with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_city = None
    error = None

    if request.method == 'POST':
        new_city = request.form.get('city', '').strip()
        if new_city:
            existing_city = City.query.filter(db.func.lower(City.name) == new_city.lower()).first()
            if not existing_city:
                city = City(name=new_city)
                db.session.add(city)
                db.session.commit()
            selected_city = new_city

    cities = City.query.order_by(City.id.desc()).all()

    if not selected_city and cities:
        selected_city = cities[0].name

    if not selected_city:
        selected_city = 'London'

    weather, fetch_error = fetch_weather(selected_city)
    if fetch_error:
        error = fetch_error

    if weather is None:
        weather = {
            'city': selected_city,
            'temperature': '--',
            'feels_like': '--',
            'description': 'Unavailable',
            'humidity': 0,
            'wind_speed': 0,
            'visibility': 0,
            'pressure': 0
        }

    return render_template('weather.html', weather=weather, error=error)


if __name__ == '__main__':
    app.run()