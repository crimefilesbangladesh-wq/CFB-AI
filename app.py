import streamlit as st
from google import genai
from duckduckgo_search import DDGS
import requests

st.set_page_config(page_title="Crime Files BD AI", layout="wide")
st.title("🚨 Crime Files BD AI (CFB AI)")

# Sidebar API Key Input
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    client = genai.Client(api_key=api_key)
    
    option = st.selectbox(
        "Choose Feature:",
        ["Fact Checking", "Automated News Writing", "Forensic Analysis", "Crime Image Generator"]
    )
    
    user_input = st.text_area("Enter News/Context/Prompt:")
    
    if st.button("Run CFB AI"):
        if option == "Fact Checking":
            with DDGS() as ddgs:
                results = list(ddgs.text(user_input, max_results=3))
            search_context = "\n".join([r['body'] for r in results])
            prompt = f"Fact check this news based on search results:\nNews: {user_input}\nSearch Context: {search_context}"
            response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
            st.write(response.text)
            
        elif option == "Automated News Writing":
            prompt = f"Write a professional investigative news report in Bangla for Crime Files BD based on this outline:\n{user_input}"
            response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
            st.write(response.text)
            
        elif option == "Forensic Analysis":
            prompt = f"Analyze this crime scenario and generate forensic questions, steps, and investigative guidelines:\n{user_input}"
            response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
            st.write(response.text)
            
        elif option == "Crime Image Generator":
            image_url = f"https://pollinations.ai/p/{requests.utils.quote(user_input)}?width=800&height=600&seed=42"
            st.image(image_url, caption="Generated Forensic Visual")
else:
    st.warning("Please enter your Gemini API Key in the sidebar to proceed.")
