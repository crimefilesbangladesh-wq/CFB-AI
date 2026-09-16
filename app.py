import streamlit as st
from google import genai

st.set_page_config(page_title="Crime Files BD AI", page_icon="🚨")
st.title("🚨 Crime Files BD")
st.subheader("বাংলাদেশের অপরাধ বিষয়ক AI")

# Sidebar for API Key
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    try:
        client = genai.Client(api_key=api_key)
        
        user_input = st.text_input("প্রশ্ন লেখো")

        if st.button("জিজ্ঞেস করো"):
            if user_input.strip() != "":
                with st.spinner("Gemini উত্তর তৈরি করছে..."):
                    response = client.models.generate_content(
                        model='gemini-1.5-flash',
                        contents=user_input
                    )
                    st.success("উত্তর:")
                    st.write(response.text)
            else:
                st.warning("অনুগ্রহ করে একটি প্রশ্ন লিখুন।")
    except Exception as e:
        st.error(f"ভুল হয়েছে: {str(e)}")
else:
    st.info("অ্যাপটি ব্যবহার করতে সাইডবারে আপনার Gemini API Key দিন।")
