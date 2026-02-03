import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

st.set_page_config(page_title="Bot Hunter V1", page_icon="🤖")

st.title("🤖 BOT HUNTER: DIRECT CHECK")
st.write("---")

emails_input = st.text_area("PASTE YOUR EMAILS TO HUNT:", height=200)

if st.button("START FAST HUNTING"):
    if not emails_input:
        st.warning("Paste emails first!")
    else:
        email_list = [e.strip() for e in emails_input.splitlines() if e.strip()]
        
        # إعدادات المتصفح الخفي (السريع)
        chrome_options = Options()
        chrome_options.add_argument("--headless") # تشغيل بدون واجهة لزيادة السرعة
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        st.info("🚀 Launching the Bot... Please wait.")
        
        try:
            # تشغيل المتصفح مرة واحدة
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            
            for email in email_list:
                driver.get("https://login.live.com/signup")
                time.sleep(1) # ننتظر التحميل
                
                input_box = driver.find_element(By.ID, "MemberName")
                input_box.clear()
                input_box.send_keys(email)
                input_box.send_keys(Keys.ENTER)
                time.sleep(1.5) # وقت كافٍ لظهور رد الفعل
                
                source = driver.page_source
                if "is already taken" in source or "Someone already" in source:
                    st.error(f"❌ {email} - TAKEN")
                else:
                    st.success(f"✅ {email} - AVAILABLE")
                    # حفظ الصيد في ملف جانبي أو عرضه بشكل مميز
            
            driver.quit()
            st.balloons()
            
        except Exception as e:
            st.error(f"Something went wrong: {e}")
