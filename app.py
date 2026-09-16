import streamlit as st

st.set_page_config(page_title="Crime Files BD", page_icon="🚨", layout="centered")

st.title("🚨 Crime Files BD")
st.write("বাংলাদেশের অপরাধ বিষয়ক AI")

st.success("অ্যাপ ঠিকঠাক চালু হয়েছে!")

prompt = st.text_input("প্রশ্ন লেখো")
if st.button("জিজ্ঞেস করো"):
    st.write(f"তুমি লিখেছো: {prompt}")
