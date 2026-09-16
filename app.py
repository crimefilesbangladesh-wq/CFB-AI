import streamlit as st
import google.generativeai as genai
from duckduckgo_search import DDGS

st.set_page_config(page_title="Crime Files BD AI", page_icon="🚨")
st.title("🚨 Crime Files BD AI (CFB AI)")

api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    option = st.selectbox(
        "Choose Feature:",
        ["Fact Checking", "Automated Investigation Support"]
    )

    user_input = st.text_area("Enter News/Context/Prompt:")

    if st.button("Run CFB AI"):
        if user_input:
            with st.spinner("CFB AI is thinking..."):
                try:
                    # Search news
                    with DDGS() as ddgs:
                        search_results = list(ddgs.text(user_input, max_results=3))
                    
                    prompt = f"Feature: {option}\nContext: {user_input}\nSearch Results: {search_results}\n\nGive a detailed Bangla fact-checked report with source links for Crime Files BD."
                    
                    response = model.generate_content(prompt)
                    st.success(response.text)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter some text!")
else:
    st.info("Please enter your Gemini API Key in sidebar to start.")
