import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

API_KEY = 'cb65223b85433968903b8215e7023d48'

@app.route('/')
def index():
    city = 'Coimbatore'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
    }

    print(weather)

    return render_template('weather.html', weather=weather)