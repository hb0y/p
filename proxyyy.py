import streamlit as st
import requests
import time

# إعدادات الواجهة
st.set_page_config(page_title="Ultra Email Checker", page_icon="🛡️", layout="centered")

st.markdown("""
    <style>
    body { background-color: #000000; color: #ffffff; }
    .stButton>button { background-color: #ff0000; color: white; width: 100%; border-radius: 12px; height: 60px; font-weight: bold; border: none; }
    .stTextArea>div>div>textarea { background-color: #050505 !important; color: #ffffff !important; border: 1px solid #ff0000 !important; }
    h1 { color: #ff0000; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ ULTRA EMAIL CHECKER")

# هنا المستخدم يحط الكود حقه لما يفتح الموقع
api_key = st.text_input("PASTE YOUR API KEY HERE:", type="password")
emails_input = st.text_area("LIST YOUR EMAILS:", height=250)

if st.button("RUN SCAN"):
    if not api_key or not emails_input:
        st.error("Please fill all fields!")
    else:
        email_list = emails_input.splitlines()
        for email in email_list:
            url = f"https://emailvalidation.abstractapi.com/v1/?api_key={api_key}&email={email.strip()}"
            try:
                data = requests.get(url).json()
                if data.get("deliverability") == "DELIVERABLE":
                    st.success(f"✅ {email} - AVAILABLE")
                else:
                    st.error(f"❌ {email} - TAKEN")
            except:
                st.write("Error checking...")
            time.sleep(0.2)
