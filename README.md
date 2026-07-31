<div align="center">

# 🌾 AI Crop Yield Prediction System

### Machine Learning-based Crop Yield Prediction using Flask, XGBoost, OpenWeather API, and Google Gemini AI

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/Flask-Web%20App-black?style=for-the-badge&logo=flask" />
<img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikit-learn" />
<img src="https://img.shields.io/badge/XGBoost-Regression-success?style=for-the-badge" />
<img src="https://img.shields.io/badge/OpenWeather-API-yellow?style=for-the-badge" />
<img src="https://img.shields.io/badge/Google-Gemini%202.5-blueviolet?style=for-the-badge&logo=google" />
</p>

**An intelligent agriculture web application that predicts crop yield using Machine Learning, fetches real-time weather information, and provides AI-powered farming assistance through Google Gemini.**

</div>

---

# 📖 Overview

The **AI Crop Yield Prediction System** is an end-to-end Machine Learning web application that predicts crop yield using agricultural and environmental parameters such as **area, crop type, rainfall, temperature, pesticides, and year**.

The application integrates **OpenWeather API** to automatically fetch live weather information and uses **Google Gemini AI** to power an intelligent farming assistant capable of answering agriculture-related questions.

This project demonstrates practical implementation of **Machine Learning, API Integration, Flask Web Development, and Cloud Deployment** for smart agriculture solutions.

---

# ✨ Key Features

- 🌾 Machine Learning-based Crop Yield Prediction
- 🌦️ Live Weather Integration using OpenWeather API
- 🤖 AI Farming Assistant powered by Google Gemini
- 📊 Interactive Prediction Dashboard
- 📱 Responsive User Interface
- ⚡ Fast Prediction using XGBoost
- 🔒 Secure API Key Management using Environment Variables
- ☁️ Ready for Cloud Deployment (Render)

---

# 🚀 Live Demo

**Web Application**

```
https://crop-yield-prediction-1-7abv.onrender.com
```


---

# 🧠 Machine Learning Workflow

```
Agricultural Data
        │
        ▼
Data Cleaning & Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
XGBoost Regression Model
        │
        ▼
Model Serialization (.pkl)
        │
        ▼
Flask Backend
        │
        ▼
Prediction Dashboard
```

---

# 📊 Input Parameters

| Parameter | Description |
|-----------|-------------|
| 🌍 Area | Country or Region |
| 🌾 Crop | Crop Name |
| 📅 Year | Prediction Year |
| 🌧 Rainfall | Annual Rainfall (mm) |
| ☀ Temperature | Average Temperature (°C) |
| 🧪 Pesticides | Pesticide Usage |

---

# 📈 Prediction Output

The application predicts the **estimated crop yield (Tonnes per Hectare)** based on the selected agricultural and weather parameters.

---

# 🛠️ Tech Stack

## Programming Language

- Python

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- Flask

## Machine Learning

- Scikit-learn
- XGBoost
- Pandas
- NumPy
- Joblib

## APIs

- OpenWeather API
- Google Gemini API

## Deployment

- Render

---

# 📂 Project Structure

```
Crop-Yield-Prediction
│
├── app
│   ├── static
│   │   ├── images
│   │   ├── style.css
│   │
│   ├── templates
│   │   └── index.html
│   │
│   ├── app.py
│   ├── chatbot.py
│   └── weather.py
│
├── models
│   ├── best_model.pkl
│   ├── area_encoder.pkl
│   └── item_encoder.pkl
│
├── outputs
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/snehamahish45/Crop-Yield-Prediction.git

cd Crop-Yield-Prediction
```

---

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a file named **`.env`**

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY
```

---

## 5️⃣ Run the Application

```bash
python -m app.app
```

Visit

```
http://127.0.0.1:5000
```

---

# 🤖 AI Farming Assistant

The integrated AI chatbot can assist users with questions related to:

- Crop Selection
- Fertilizer Recommendations
- Pest Control
- Irrigation Methods
- Farming Best Practices
- Weather-related Guidance
- General Agriculture Knowledge

The chatbot is powered by **Google Gemini 2.5 Flash** using the official **google-genai** SDK.

---

# 🌦 Weather Integration

The application fetches real-time weather information from the **OpenWeather API**, including:

- Temperature
- Humidity
- Weather Condition

These values are automatically used to improve crop yield prediction.

---

# 📦 Requirements

- Flask
- Requests
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Joblib
- Google GenAI SDK
- Python-dotenv

---

# 💼 Skills Demonstrated

- Machine Learning
- Data Preprocessing
- Feature Engineering
- XGBoost Regression
- Flask Web Development
- REST API Integration
- Google Gemini AI Integration
- OpenWeather API Integration
- Environment Variable Management
- Cloud Deployment (Render)
- Git & GitHub

---

# 🚀 Future Enhancements

- 🌱 Crop Recommendation System
- 🌿 Fertilizer Recommendation
- 🦠 Plant Disease Detection using Deep Learning
- 🌍 Multi-language Support
- 🎤 Voice-enabled AI Assistant
- 📊 Prediction History Dashboard
- 👤 User Authentication
- 📱 Mobile Application

---

# 👨‍💻 Author

## Sneha Mahish

**B.Tech Computer Science (AI & ML)**

📧 Email: **snehamahish51@gmail.com**

🔗 LinkedIn: https://www.linkedin.com/in/sneha-mahish-03b56033b/

💻 GitHub: https://github.com/snehamahish45

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

# 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

### 🌾 Empowering Smart Agriculture with Artificial Intelligence

**Made with ❤️ by Sneha Mahish**

</div><div align="center">

# 🌾 AI Crop Yield Prediction System

### Machine Learning-based Crop Yield Prediction using Flask, XGBoost, OpenWeather API, and Google Gemini AI

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/Flask-Web%20App-black?style=for-the-badge&logo=flask" />
<img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikit-learn" />
<img src="https://img.shields.io/badge/XGBoost-Regression-success?style=for-the-badge" />
<img src="https://img.shields.io/badge/OpenWeather-API-yellow?style=for-the-badge" />
<img src="https://img.shields.io/badge/Google-Gemini%202.5-blueviolet?style=for-the-badge&logo=google" />
</p>

**An intelligent agriculture web application that predicts crop yield using Machine Learning, fetches real-time weather information, and provides AI-powered farming assistance through Google Gemini.**

</div>

---

# 📖 Overview

The **AI Crop Yield Prediction System** is an end-to-end Machine Learning web application that predicts crop yield using agricultural and environmental parameters such as **area, crop type, rainfall, temperature, pesticides, and year**.

The application integrates **OpenWeather API** to automatically fetch live weather information and uses **Google Gemini AI** to power an intelligent farming assistant capable of answering agriculture-related questions.

This project demonstrates practical implementation of **Machine Learning, API Integration, Flask Web Development, and Cloud Deployment** for smart agriculture solutions.

---

# ✨ Key Features

- 🌾 Machine Learning-based Crop Yield Prediction
- 🌦️ Live Weather Integration using OpenWeather API
- 🤖 AI Farming Assistant powered by Google Gemini
- 📊 Interactive Prediction Dashboard
- 📱 Responsive User Interface
- ⚡ Fast Prediction using XGBoost
- 🔒 Secure API Key Management using Environment Variables
- ☁️ Ready for Cloud Deployment (Render)

---

# 🚀 Live Demo

**Web Application**

```
https://your-render-url.onrender.com
```

*(Replace with your deployed Render URL.)*

---

# 🧠 Machine Learning Workflow

```
Agricultural Data
        │
        ▼
Data Cleaning & Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
XGBoost Regression Model
        │
        ▼
Model Serialization (.pkl)
        │
        ▼
Flask Backend
        │
        ▼
Prediction Dashboard
```

---

# 📊 Input Parameters

| Parameter | Description |
|-----------|-------------|
| 🌍 Area | Country or Region |
| 🌾 Crop | Crop Name |
| 📅 Year | Prediction Year |
| 🌧 Rainfall | Annual Rainfall (mm) |
| ☀ Temperature | Average Temperature (°C) |
| 🧪 Pesticides | Pesticide Usage |

---

# 📈 Prediction Output

The application predicts the **estimated crop yield (Tonnes per Hectare)** based on the selected agricultural and weather parameters.

---

# 🛠️ Tech Stack

## Programming Language

- Python

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- Flask

## Machine Learning

- Scikit-learn
- XGBoost
- Pandas
- NumPy
- Joblib

## APIs

- OpenWeather API
- Google Gemini API

## Deployment

- Render

---

# 📂 Project Structure

```
Crop-Yield-Prediction
│
├── app
│   ├── static
│   │   ├── images
│   │   ├── style.css
│   │
│   ├── templates
│   │   └── index.html
│   │
│   ├── app.py
│   ├── chatbot.py
│   └── weather.py
│
├── models
│   ├── best_model.pkl
│   ├── area_encoder.pkl
│   └── item_encoder.pkl
│
├── outputs
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/snehamahish45/Crop-Yield-Prediction.git

cd Crop-Yield-Prediction
```

---

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a file named **`.env`**

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY
```

---

## 5️⃣ Run the Application

```bash
python -m app.app
```

Visit

```
http://127.0.0.1:5000
```

---

# 🤖 AI Farming Assistant

The integrated AI chatbot can assist users with questions related to:

- Crop Selection
- Fertilizer Recommendations
- Pest Control
- Irrigation Methods
- Farming Best Practices
- Weather-related Guidance
- General Agriculture Knowledge

The chatbot is powered by **Google Gemini 2.5 Flash** using the official **google-genai** SDK.

---

# 🌦 Weather Integration

The application fetches real-time weather information from the **OpenWeather API**, including:

- Temperature
- Humidity
- Weather Condition

These values are automatically used to improve crop yield prediction.

---

# 📦 Requirements

- Flask
- Requests
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Joblib
- Google GenAI SDK
- Python-dotenv

---

# 💼 Skills Demonstrated

- Machine Learning
- Data Preprocessing
- Feature Engineering
- XGBoost Regression
- Flask Web Development
- REST API Integration
- Google Gemini AI Integration
- OpenWeather API Integration
- Environment Variable Management
- Cloud Deployment (Render)
- Git & GitHub

---

# 🚀 Future Enhancements

- 🌱 Crop Recommendation System
- 🌿 Fertilizer Recommendation
- 🦠 Plant Disease Detection using Deep Learning
- 🌍 Multi-language Support
- 🎤 Voice-enabled AI Assistant
- 📊 Prediction History Dashboard
- 👤 User Authentication
- 📱 Mobile Application

---

# 👨‍💻 Author

## Sneha Mahish

**B.Tech Computer Science (AI & ML)**

📧 Email: **snehamahish51@gmail.com**

🔗 LinkedIn: https://www.linkedin.com/in/sneha-mahish-03b56033b/

💻 GitHub: https://github.com/snehamahish45

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

# 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

### 🌾 Empowering Smart Agriculture with Artificial Intelligence

**Made with ❤️ by Sneha Mahish**

</div>
