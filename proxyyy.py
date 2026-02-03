import streamlit as st
import requests
import time

# --- تصميم الواجهة الرهيبة ---
st.set_page_config(page_title="Pro API Checker", page_icon="🛡️")

st.markdown("""
    <style>
    body { background-color: #000000; color: #ffffff; }
    .stButton>button { background-color: #ff0000; color: white; width: 100%; font-weight: bold; border-radius: 8px; border: none; }
    .stTextInput>div>div>input { background-color: #111 !important; color: white !important; }
    .result-card { padding: 10px; border-radius: 5px; margin-bottom: 5px; border-right: 5px solid #ff0000; background: #0f0f0f; }
    h1 { color: #ff0000; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ HOBK IS HERE")

# إدخال الـ API Key
api_key = st.text_input("ENTER YOUR API KEY (6d88...):", type="password")
emails_input = st.text_area("LIST YOUR EMAILS (ONE PER LINE):", height=200)

if st.button("START DEEP VERIFICATION"):
    if not api_key or not emails_input:
        st.warning("Please fill in both fields!")
    else:
        email_list = [e.strip() for e in emails_input.splitlines() if e.strip()]
        st.info(f"Checking {len(email_list)} emails...")
        
        for email in email_list:
            # طلب البيانات من Abstract API
            url = f"https://emailvalidation.abstractapi.com/v1/?api_key={api_key}&email={email}"
            
            try:
                response = requests.get(url)
                data = response.json()
                
                # تحليل النتيجة: الفحص الحقيقي
                # بنشيك على الـ Score (إذا كان أقل من 0.50 يعني غالباً متاح)
                # وبنشيك على الـ deliverability
                deliverability = data.get("deliverability")
                quality_score = float(data.get("quality_score", 0))

                if deliverability == "UNDELIVERABLE" or quality_score < 0.10:
                    st.success(f"✅ AVAILABLE: {email} (Score: {quality_score})")
                else:
                    st.error(f"❌ TAKEN: {email} (Score: {quality_score})")
                
            except Exception as e:
                st.write(f"⚠️ Error checking {email}")
            
            # تأخير بسيط عشان ليمت الـ API
            time.sleep(0.5)
