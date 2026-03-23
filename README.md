# 🌦️ Aethen Weather App

Aethen Weather App is a lightweight and user-friendly weather application built using Flask. It allows users to fetch real-time weather data for any city using an external weather API and displays it in a clean and intuitive interface.

---

## 🚀 Features

* 🌍 Search weather by city name
* 🌡️ Displays real-time temperature and weather conditions
* 📡 Integrated with external weather API
* ⚡ Fast and lightweight Flask backend
* 🎨 Simple and responsive UI

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS
* **API:** OpenWeather API (or the API you used)
* **Version Control:** Git & GitHub

---

## 📁 Project Structure

```
weather-app/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── styles.css
└── README.md
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1. Clone the repository

```
git clone https://github.com/your-username/weather-app.git
```

### 2. Navigate to project directory

```
cd weather-app
```

### 3. Create a virtual environment

```
python -m venv venv
```

### 4. Activate the virtual environment

* **Windows:**

```
venv\Scripts\activate
```

* **Mac/Linux:**

```
source venv/bin/activate
```

### 5. Install dependencies

```
pip install -r requirements.txt
```

### 6. Run the application

```
python app.py
```

### 7. Open in browser

```
http://127.0.0.1:5000/
```

---

## 🔑 API Configuration

This app requires a weather API key.

1. Get your API key from OpenWeather:
   https://openweathermap.org/api

2. Add your API key in the code (e.g., in `app.py`):

```
API_KEY = "your_api_key_here"
```

> ⚠️ Important: Do NOT expose your API key in public repositories. Use environment variables for better security.

---

## 📸 Screenshots

*Add screenshots of your application here to showcase UI and functionality.*

---

## 📌 Future Enhancements

* 🌤️ 7-day weather forecast
* 📍 Auto-detect user location
* 📊 Weather analytics and charts
* 🌙 Dark mode support
* 📱 Fully responsive mobile UI

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Utkarsh**

* GitHub: https://github.com/your-username

---

## ⭐ Acknowledgements

* OpenWeather API for providing weather data
* Flask documentation for backend support

---

⭐ If you found this project helpful, consider giving it a star!
