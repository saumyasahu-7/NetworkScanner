import streamlit as st
import requests

# Set up the Streamlit app
st.title("Network Scanner")

# Welcome message
st.write("Welcome to the Network Scanning Application!")

# Input field for the user's name
name = st.text_input("Enter your name")

# Display a personalized welcome message
if name:
    st.write(f"Hello, {name}! Ready to scan your network?")

# Button to start scanning
if st.button("Start Scanning"):
    try:
        response = requests.get("http://127.0.0.1:5001/check_threats")
        if response.status_code == 200:
            response_data = response.json()
            message = response_data.get("msg", "No message received")
            st.success(f"✅ {message}")
        else:
            st.error(f"❌ Failed to start scanning. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"⚠️ An error occurred: {e}")
