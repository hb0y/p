import streamlit as st
import requests
import time

# --- تصميم الواجهة ---
st.set_page_config(page_title="Ultra Email Checker", page_icon="🛡️")
st.markdown("<style>body{background-color:black;color:white;}.stButton>button{background-color:red;color:white;width:100%;font-weight:bold;}</style>", unsafe_allow_html=True)

st.title("🛡️ ULTRA EMAIL CHECKER")

api_key = st.text_input("PASTE YOUR API KEY HERE:", type="password")
emails_input = st.text_area("LIST YOUR EMAILS:", height=200)

if st.button("RUN DEEP SCAN"):
    if not api_key or not emails_input:
        st.error("Please fill all fields!")
    else:
        email_list = [e.strip() for e in emails_input.splitlines() if e.strip()]
        st.info(f"Scanning {len(email_list)} emails... Showing ONLY available results.")
        
        available_emails = []
        
        for email in email_list:
            url = f"https://emailvalidation.abstractapi.com/v1/?api_key={api_key}&email={email}"
            try:
                response = requests.get(url)
                data = response.json()
                
                # منطق فحص أكثر ذكاءً
                is_taken = data.get("is_disposable_address", {}).get("value", False) or \
                           data.get("deliverability") == "UNDELIVERABLE"
                
                # إذا لم يكن محجوزاً يقيناً، نعتبره متاح للتجربة
                if data.get("deliverability") == "DELIVERABLE":
                    available_emails.append(email)
                    st.success(f"✅ FOUND: {email}")
                
            except:
                pass # تجاهل الأخطاء للاستمرار في الفحص
            
            time.sleep(0.3) # سرعة معقولة

        if available_emails:
            st.markdown("### 📥 Available List:")
            st.text_area("Copy from here:", value="\n".join(available_emails))
            st.download_button("Download .txt", "\n".join(available_emails), "available_emails.txt")
        else:
            st.warning("No available emails found in this batch. Try longer combinations!")
