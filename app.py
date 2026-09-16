import streamlit as st

st.set_page_config(page_title="Crime Files BD", page_icon="🚨", layout="centered")

st.markdown("### 🚨 Crime Files BD")
st.write("বাংলাদেশের অপরাধ বিষয়ক তথ্য সহায়তা")
st.success("অ্যাপ সফলভাবে চালু হয়েছে!")
st.divider()

q = st.text_input("এখানে তোমার প্রশ্ন লেখো")
if st.button("জিজ্ঞেস করো"):
    if q:
        st.write(f"তুমি লিখেছো: {q}")
        st.write("এটা কাজ করছে বন্ধু! এখন আমরা AI যোগ করবো।")
    else:
        st.warning("প্রশ্ন লেখো বন্ধু")
