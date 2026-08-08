### 🌤️ Weather Analyst AI

Weather Analyst AI is a Python-based weather application built using
Streamlit, OpenWeatherMap API, and Ollama.

It provides weather information for a city and uses AI to generate
weather analysis and precautions.

## 🚀 Features

- 🌍 Search weather by city name
- 🌡️ Display current temperature
- 💧 Display humidity
- 💨 Display wind information
- 🤖 AI-powered weather analysis
- ⚠️ Weather precautions and recommendations
- 🖥️ Simple Streamlit web interface

## 🛠️ Technologies Used

- Python
- Streamlit
- OpenWeatherMap API
- Ollama
- Requests

## 📋 Requirements

Make sure you have installed:

1. Python 3.10 or higher
2. Ollama
3. Git

## 📦 Installation

### 1. Clone the repository

``bash
git clone https://github.com/maneeshchittem-hub/weather_ollamamodel.git
### 2. Open the project folder
cd weather_ollamamodel
### 3. Create a virtual environment
python -m venv myenv
### 4. Activate the virtual environment
Windows:
myenv\Scripts\activate
### 5. Install required Python packages
pip install streamlit requests ollama
## 🤖 Ollama Setup
Install Ollama on your computer.
Then download the required AI model:
ollama pull llama3.2
Start Ollama:
ollama serve
## 🔑 OpenWeatherMap API
Create an account on OpenWeatherMap and get your API key.
Add your API key to the Python application.
⚠️ Do not upload your API key publicly to GitHub.
## ▶️ Run the Application
Run:
streamlit run weather.py
The application will open in your browser.
## 📁 Project Structure
weather_ollamamodel/
│
├── weather.py
├── README.md
└── ...
## 🖥️ How It Works
Enter a city name.
Click Get Weather & Precautions.
The application gets weather information from OpenWeatherMap.
Ollama analyzes the weather information.
The application displays weather precautions and recommendations.
## 🔮 Future Improvements
-5-day weather forcast
-weather maps
-voice assistant
-multiple Ai models
-weather alerts
## 👨‍💻 Author
**Maneesh Chittem**
GitHub: maneeshchittem-hub
## ⭐ Support
If you like this project, give the repository a ⭐ on GitHub!
