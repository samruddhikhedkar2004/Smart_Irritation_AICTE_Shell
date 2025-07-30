import streamlit as st
import numpy as np
import joblib  

# --- Page Config ---
st.set_page_config(page_title="Smart Sprinkler System", page_icon="💧", layout="centered")

# --- Header ---
st.title("💧 Smart Sprinkler System")
st.markdown("""
This project is a part of **AICTE Internship Cycle 2**  
**Prepared by: Samruddhi Khedkar**  
""")

st.subheader("Enter the scaled sensor values (0 to 1) to predict sprinkler status")

# --- Load Model ---
model = joblib.load("Farm_Irrigation_System.pkl")  

# --- Input Section ---
sensor_values = []
st.markdown("### 🌱 Sensor Inputs:")
for i in range(20):
    val = st.slider(f"Sensor {i+1}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    sensor_values.append(val)

# --- Predict Button ---
if st.button("🔍 Predict Sprinkler Status"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    # --- Results Section ---
    st.markdown("## 🔔 Prediction Results:")
    for i, status in enumerate(prediction):
        if status == 1:
            st.success(f"Sprinkler {i+1} (Parcel_{i+1}): **ON** ✅")
        else:
            st.error(f"Sprinkler {i+1} (Parcel_{i+1}): **OFF** ❌")

# --- Footer ---
st.markdown("---")
st.caption("💡 *Improved with Streamlit UI and dynamic visuals for better user experience.*")
