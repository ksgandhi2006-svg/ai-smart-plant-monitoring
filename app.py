import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Smart Plant Monitor",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 AI-Based Smart Plant Monitoring System")
st.write("Smart monitoring and automatic irrigation using IoT and AI/ML")

st.divider()

# Plant selection
plant = st.selectbox(
    "🌿 Select Plant",
    ["Money Plant", "Rose", "Tulsi", "Aloe Vera"]
)

# Demo sensor values
soil_moisture = 32
temperature = 28
humidity = 56

# AI prediction
if soil_moisture < 40:
    prediction = "⚠️ Water Required"
    pump_status = "🟢 ON"
else:
    prediction = "✅ No Water Required"
    pump_status = "🔴 OFF"

# Sensor values
st.subheader("📊 Current Sensor Readings")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌱 Soil Moisture", f"{soil_moisture}%")

with col2:
    st.metric("🌡️ Temperature", f"{temperature} °C")

with col3:
    st.metric("💧 Humidity", f"{humidity}%")

st.divider()

# AI section
st.subheader("🤖 AI / ML Prediction")

col1, col2 = st.columns(2)

with col1:
    st.info(f"Plant: {plant}")
    st.warning(prediction)

with col2:
    st.success(f"Pump Status: {pump_status}")

st.divider()

# Chart
st.subheader("📈 Environmental Data")

data = pd.DataFrame({
    "Parameter": [
        "Soil Moisture",
        "Temperature",
        "Humidity"
    ],
    "Value": [
        soil_moisture,
        temperature,
        humidity
    ]
})

st.bar_chart(data.set_index("Parameter"))

st.divider()

st.subheader("💡 System Status")

st.write("✅ Sensors connected")
st.write("✅ AI model ready")
st.write("✅ Irrigation system ready")

st.caption(
    "AI Smart Plant Monitoring and Automatic Irrigation System"
)