import streamlit as st
import requests
import time

# --- إعدادات الواجهة الرهيبة ---
st.set_page_config(page_title="Ultra Email Checker", page_icon="🛡️", layout="centered")

st.markdown("""
    <style>
    body { background-color: #000000; color: #ffffff; }
    .stButton>button { 
        background-color: #ff0000; color: white; width: 100%; border-radius: 12px; 
        height: 60px; font-size: 20px; font-weight: bold; border: none; transition: 0.5s;
    }
    .stButton>button:hover { background-color: #990000; box-shadow: 0px 0px 30px #ff0000; cursor: pointer; }
    .stTextArea>div>div>textarea { background-color: #050505 !important; color: #ffffff !important; border: 1px solid #ff0000 !important; }
    .result-card { padding: 15px; border-radius: 10px; margin-bottom: 10px; border-right: 8px solid #ff0000; background-color: #111; display: flex; justify-content: space-between; align-items: center; }
    h1 { color: #ff0000; text-align: center; font-weight: 900; letter-spacing: 3px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ ULTRA EMAIL CHECKER")
st.write("---")

# خانة الـ API Key
api_key = st.text_input("PASTE YOUR ABSTRACT API KEY HERE:", type="password")

# خانة وضع الإيميلات
emails_input = st.text_area("LIST YOUR EMAILS (ONE PER LINE):", height=250)

if st.button("RUN DEEP SCAN"):
    if not api_key:
        st.error("❗ PLEASE ENTER YOUR API KEY FIRST")
    elif not emails_input:
        st.warning("❗ PLEASE PASTE EMAILS TO SCAN")
    else:
        email_list = [e.strip() for e in emails_input.splitlines() if e.strip()]
        st.info(f"🚀 Scanning {len(email_list)} emails... Please wait.")
        
        valid_count = 0
        invalid_count = 0
        
        # مكان عرض النتائج المباشرة
        results_container = st.container()

        for email in email_list:
            # طلب الفحص من السيرفر
            url = f"https://emailvalidation.abstractapi.com/v1/?api_key={api_key}&email={email}"
            
            try:
                response = requests.get(url)
                data = response.json()
                
                # التحقق الحقيقي: هل الإيميل موجود؟
                # deliverability: DELIVERABLE يعني موجود وشغال
                is_valid = data.get("deliverability") == "DELIVERABLE"
                
                if is_valid:
                    valid_count += 1
                    st.markdown(f"<div class='result-card' style='border-color: #00ff00;'><span>✅ <b>{email}</b></span> <span style='color:#00ff00'>AVAILABLE</span></div>", unsafe_allow_html=True)
                else:
                    invalid_count += 1
                    st.markdown(f"<div class='result-card' style='border-color: #ff0000;'><span>❌ <b>{email}</b></span> <span style='color:#ff0000'>TAKEN / INVALID</span></div>", unsafe_allow_html=True)
                
            except:
                st.error(f"Error checking {email}")
            
            # احتراماً لسرعة الـ API المجاني
            time.sleep(0.3)

        st.balloons()
        st.success("SCAN COMPLETED!")
        
        # ملخص نهائي
        c1, c2 = st.columns(2)
        c1.metric("AVAILABLE ✅", valid_count)
        c2.metric("TAKEN/INVALID ❌", invalid_count)
        
