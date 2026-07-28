import streamlit as st
import requests
import json

API_URL = "http://localhost:8000/predict" 

st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    # try:
    #     response = requests.post(API_URL, json=input_data)
    #     result = response.json()

    #     if response.status_code == 200 and "response" in result:
    #         prediction = result["response"]
    #         st.success(f"Predicted Insurance Premium Category: **{prediction['predicted_category']}**")
    #         st.write("🔍 Confidence:", prediction["confidence"])
    #         st.write("📊 Class Probabilities:")
    #         st.markdown(prediction["class_probabilities"])

    #     else:
    #         st.error(f"API Error: {response.status_code}")
    #         st.write(result)

    # except requests.exceptions.ConnectionError:
    #     st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")

    try:
        response = requests.post(API_URL, json=input_data, timeout=10)
        response.raise_for_status()
        result = response.json()

        if isinstance(result, dict) and "response" in result:
            prediction = result["response"]

            st.subheader("Prediction Result")
            st.success(f"Predicted Premium Category: **{prediction['predicted_category']}**")

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Confidence", f"{prediction.get('confidence', 0):.2f}")
            with col2:
                st.metric("Input City", city)

            st.write("### Class Probabilities")
            probabilities = prediction.get("class_probabilities", {})
            if probabilities:
                for label, value in probabilities.items():
                    st.write(f"- {label}: {value:.2f}")
            else:
                st.info("No Probability Data Available.")

        else:
            st.error("Unexpected response from the API.")
            st.json(result)

    except requests.exceptions.Timeout:
        st.error("The request timed out. Please check the API server.")
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")