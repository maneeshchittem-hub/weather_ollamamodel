
import requests as req
import streamlit as st
from ollama import Client

# ---------------- Page ----------------
st.set_page_config(
    page_title="Weather Analyst AI",
    page_icon="🌤️"
)

st.title("🌤️ Weather Analyst AI")

city = st.text_input("Enter City Name")

if st.button("Get Weather & Precautions"):

    # ---------------- Weather API ----------------
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=389d821ff0165a8fa4c6319e8ae6c92f"

    res = req.get(url)
    weather = res.json()

    if res.status_code != 200:
        st.error("City not found")
    else:

        # ---------------- Weather ----------------
        st.subheader("🌤️ Current Weather")

        st.write("City:", weather["name"])
        st.write("Weather:", weather["weather"][0]["main"])
        st.write("Description:", weather["weather"][0]["description"])
        st.write("Temperature:", f"{weather['main']['temp'] - 273.15:.1f} °C")
        st.write("Feels Like:", f"{weather['main']['feels_like'] - 273.15:.1f} °C")
        st.write("Humidity:", weather["main"]["humidity"], "%")
        st.write("Wind Speed:", weather["wind"]["speed"], "m/s")

        st.divider()

        # ---------------- Ollama AI ----------------
        st.subheader("🤖 AI Precautions")

        prompt = f"""
        You are a weather analyst.

        Weather data:
        {weather}

        Give only:
        1. Food precautions
        2. Clothing precautions

        Use bullet points only.
        """

        client = Client()

        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        output = st.empty()
        answer = ""

        for part in client.chat(
            "llama3.2:1b",
            messages=messages,
            stream=True
        ):
            answer += part.message.content
            output.markdown(answer)
