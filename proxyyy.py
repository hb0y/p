import streamlit as st
import requests
import time

st.set_page_config(page_title="MS Ultra Hunter", page_icon="🎯")

st.markdown("""
    <style>
    body { background-color: #000; color: #fff; }
    .stButton>button { background: linear-gradient(45deg, #ff0000, #990000); color:white; border:none; height:50px; width:100%; border-radius:10px; font-weight:bold; }
    .result-box { padding:15px; border-radius:10px; margin-bottom:10px; background:#111; border-left: 5px solid #ff0000; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 MS ULTRA HUNTER")
st.write("---")

emails_input = st.text_area("PASTE EMAILS (NO API / NO BROWSER):", height=200)

if st.button("START DEEP SCAN"):
    if not emails_input:
        st.warning("Please paste emails!")
    else:
        email_list = [e.strip() for e in emails_input.splitlines() if e.strip()]
        st.info(f"🔍 Scanning {len(email_list)} emails using MS Pre-Auth Bypass...")
        
        for email in email_list:
            # رابط الفحص الرسمي من مايكروسوفت (المستخدم في التطبيقات)
            url = "https://login.microsoftonline.com/common/GetCredentialType"
            
            payload = {
                "username": email,
                "isOtherIdpSupported": True,
                "checkRemoteGWContext": True,
                "type": 1,
                "flowToken": "1"
            }
            
            try:
                # محاكاة طلب من متصفح حقيقي لتجنب الحظر
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
                response = requests.post(url, json=payload, headers=headers)
                data = response.json()
                
                # IfExistsResult == 0 يعني الإيميل موجود (Taken)
                # IfExistsResult == 5 يعني الإيميل غير موجود (Available)
                result = data.get("IfExistsResult")
                
                if result == 5:
                    st.success(f"✅ AVAILABLE: {email}")
                elif result == 0:
                    st.error(f"❌ TAKEN: {email}")
                else:
                    st.warning(f"⚠️ UNKNOWN: {email}")
                    
            except:
                st.write(f"Error checking {email}")
            
            time.sleep(0.5) # سرعة خرافية مع أمان

        st.balloons()
