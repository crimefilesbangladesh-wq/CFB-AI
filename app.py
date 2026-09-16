import streamlit as st
import google.generativeai as genai
import os

# পেজ সেটআপ - যাতে মোবাইলে কেটে না যায়
st.set_page_config(
    page_title="Crime Files Bangladesh",
    page_icon="🚨",
    layout="centered"
)

# CSS - লেখা যাতে না কাটে
st.markdown("""
<style>
    .main-title {
        font-size: 28px !important;
        font-weight: bold;
        text-align: center;
        white-space: normal !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🚨 Crime Files Bangladesh AI</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>বাংলাদেশের অপরাধ বিষয়ক তথ্য ও সহায়তা</p>", unsafe_allow_html=True)
st.divider()

# API Key - Streamlit Secrets থেকে নিবে
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except:
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API Key পাওয়া যায়নি! Streamlit Secrets এ GEMINI_API_KEY যোগ করো।")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User
