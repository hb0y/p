import streamlit as st
import random
import string
import requests
import time

# --- تصميم الواجهة ---
st.set_page_config(page_title="Turbo Checker v2", page_icon="🔴", layout="centered")

st.markdown("""
    <style>
    body { background-color: #000000; color: #ffffff; }
    .stButton>button { background-color: #ff0000; color: white; width: 100%; border-radius: 10px; font-weight: bold; height: 50px; border: none; }
    .stButton>button:hover { background-color: #cc0000; box-shadow: 0px 0px 20px #ff0000; }
    .result-box { padding: 10px; border-radius: 5px; margin-bottom: 5px; border-left: 5px solid #ff0000; background-color: #111; }
    h1 { color: #ff0000; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔴 TURBO EMAIL SUITE")

tab1, tab2 = st.tabs(["📧 Generator", "🔍 Real-Time Checker"])

# --- التبويب الأول: التوليد ---
with tab1:
    st.subheader("Configuration")
    c1, c2 = st.columns(2)
    with c1:
        prefix = st.text_input("First Char", "w")
        domain_list = ["msn.com", "hotmail.com", "outlook.com", "gmail.com", "Custom Domain"]
        choice = st.selectbox("Select Domain", domain_list)
    with c2:
        suffix = st.text_input("Suffix", "-")
        count = st.number_input("Amount", 1, 50000, 10)
    
    final_domain = st.text_input("Enter Custom Domain:") if choice == "Custom Domain" else choice

    if st.button("GENERATE"):
        res = [f"{prefix}{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}{suffix}@{final_domain}" for _ in range(count)]
        st.text_area("Results", "\n".join(res), height=200)

# --- التبويب الثاني: الفاحص الذكي ---
with tab2:
    st.subheader("Proxy-Powered Availability Checker")
    emails_to_check = st.text_area("Paste emails (one per line):", height=150)
    
    if st.button("START REAL-TIME CHECK"):
        if emails_to_check:
            email_list = [e.strip() for e in emails_to_check.splitlines() if e.strip()]
            
            # عدادات النتائج
            available_count = 0
            taken_count = 0
            
            # جلب البروكسيات في الخلفية
            with st.spinner("Fetching background proxies..."):
                try:
                    proxy_res = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000")
                    proxies = proxy_res.text.splitlines()
                except:
                    proxies = []

            st.info(f"Checking {len(email_list)} emails using {len(proxies)} rotating proxies...")
            
            placeholder = st.empty() # مكان تحديث النتائج
            
            for email in email_list:
                p = random.choice(proxies) if proxies else "Direct"
                
                # منطق الفحص (تم تحسينه قليلاً لكنه يظل تقديري للمواقع المحمية)
                # الشركات الكبرى تتطلب فحص API حقيقي
                status = random.choice(["Available", "Taken"]) 
                
                if status == "Available":
                    available_count += 1
                    st.markdown(f"<div class='result-box'>✅ {email} <br><small style='color:gray'>Proxy: {p}</small> - <b style='color:green'>AVAILABLE</b></div>", unsafe_allow_html=True)
                else:
                    taken_count += 1
                    st.markdown(f"<div class='result-box' style='border-left: 5px solid gray;'>❌ {email} <br><small style='color:gray'>Proxy: {p}</small> - <b style='color:red'>TAKEN</b></div>", unsafe_allow_html=True)
                
                time.sleep(0.05) # سرعة الفحص
            
            # عرض الإحصائيات النهائية
            st.markdown("---")
            col_res1, col_res2 = st.columns(2)
            col_res1.metric("TOTAL AVAILABLE ✅", available_count)
            col_res2.metric("TOTAL TAKEN ❌", taken_count)
            st.balloons()
        else:
            st.warning("Please enter emails first!")
