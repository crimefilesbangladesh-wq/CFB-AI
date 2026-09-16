import streamlit as st
from google import genai
from duckduckgo_search import DDGS
import requests

st.set_page_config(page_title="Crime Files BD AI", page_icon="🚨")
st.title("🚨 Crime Files BD AI (CFB AI)")

# Sidebar API Key Input
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    try:
        client = genai.Client(api_key=api_key)

        option = st.selectbox(
            "Choose Feature:",
            ["Fact Checking", "Automated Investigation Support"]
        )

        user_input = st.text_area("Enter News/Context/Prompt:")

        if st.button("Run CFB AI"):
            if user_input.strip() != "":
                with st.spinner("Analyzing with Gemini AI..."):
                    prompt = f"Feature: {option}\nInput: {user_input}\nProvide a detailed and accurate response."
                    
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt
                    )
                    
                    st.subheader("Result:")
                    st.write(response.text)
            else:
                st.warning("Please enter some text to process.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
else:
    st.info("Please enter your Gemini API Key in the sidebar to proceed.")
    
