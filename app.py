import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("fake_currency_model_compressed.pkl")

# Streamlit UI
st.title("Fake Currency Detection")
st.write("Enter the details of the currency note:")

# Create input fields
diagonal = st.number_input("Diagonal Length (mm)", min_value=100.0, max_value=200.0, step=0.01)
height_left = st.number_input("Height Left (mm)", min_value=50.0, max_value=150.0, step=0.01)
height_right = st.number_input("Height Right (mm)", min_value=50.0, max_value=150.0, step=0.01)
margin_low = st.number_input("Lower Margin (mm)", min_value=1.0, max_value=10.0, step=0.01)
margin_up = st.number_input("Upper Margin (mm)", min_value=1.0, max_value=10.0, step=0.01)
length = st.number_input("Length (mm)", min_value=100.0, max_value=200.0, step=0.01)

# Predict button
if st.button("Check Authenticity"):
    # Create DataFrame with user inputs
    input_data = pd.DataFrame([[diagonal, height_left, height_right, margin_low, margin_up, length]],
                              columns=["diagonal", "height_left", "height_right", "margin_low", "margin_up", "length"])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Show result
    if prediction[0] == 1:
        st.success("✅ This is a **Genuine** currency note.")
    else:
        st.error("❌ This is a **Fake** currency note.")
