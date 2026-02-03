import streamlit as st
import random
import string
import requests

# إعداد الصفحة والثيم
st.set_page_config(page_title="Email Pro Suite", page_icon="🔴", layout="centered")

st.markdown("""
    <style>
    html, body, [class*="css"] { background-color: #000000; color: #ffffff; font-family: 'Inter', sans-serif; }
    .stButton>button { width: 100%; background-color: #ff0000; color: white; border-radius: 8px; font-weight: bold; border: none; padding: 15px; }
    .stButton>button:hover { background-color: #990000; box-shadow: 0px 0px 15px #ff0000; }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea { background-color: #0f0f0f !important; color: white !important; border: 1px solid #440000 !important; }
    h1 { color: #ff0000; text-align: center; letter-spacing: 2px; }
    </style>
    """, unsafe_allow_html=True)

# دالة لجلب البروكيسات تلقائياً في الخلفية
def get_free_proxies():
    try:
        # نجلب قائمة بروكيسات مجانية محدثة
        response = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
        if response.status_code == 200:
            proxies = response.text.split('\r\n')
            return [p for p in proxies if p]
    except:
        return []
    return []

st.title("🔴 EMAIL PRO TOOLS")

tab1, tab2 = st.tabs(["📧 Generator", "🔍 Turbo Checker (Auto-Proxy)"])

with tab1:
    st.subheader("Configuration")
    c1, c2 = st.columns(2)
    with c1:
        prefix = st.text_input("Start Letter", "s")
        domain = st.selectbox("Domain", ["msn.com", "hotmail.com", "gmail.com", "outlook.com", "Custom"])
    with c2:
        suffix = st.text_input("Suffix", "-")
        count = st.number_input("Amount", 1, 10000, 10)
    
    if domain == "Custom":
        domain = st.text_input("Type Domain:")

    if st.button("GENERATE LIST"):
        results = [f"{prefix}{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}{suffix}@{domain}" for _ in range(count)]
        st.text_area("Generated Emails", "\n".join(results), height=200)

with tab2:
    st.subheader("Turbo Availability Check")
    emails_input = st.text_area("Paste emails to check (one per line):", height=150)
    
    if st.button("START CHECKING"):
        if emails_input:
            email_list = emails_input.split('\n')
            proxies = get_free_proxies() # جلب البروكيسات تلقائياً
            
            if not proxies:
                st.error("Could not fetch proxies. Using direct connection (Risk of Ban).")
            else:
                st.success(f"Successfully loaded {len(proxies)} background proxies for speed!")

            # محاكاة الفحص (بما أن الفحص الحقيقي يتطلب اتصال SMTP معقد)
            progress_bar = st.progress(0)
            for i, email in enumerate(email_list):
                # هنا نختار بروكسي عشوائي لكل عملية فحص
                current_proxy = random.choice(proxies) if proxies else "Direct"
                
                # ملاحظة للمبرمج: هنا نضع كود فحص الـ SMTP باستخدام 'current_proxy'
                # حالياً سأعطيك محاكاة للنتائج لتجربة الواجهة
                st.write(f"Checking {email.strip()} via {current_proxy}...")
                progress_bar.progress((i + 1) / len(email_list))
            
            st.balloons()
            st.success("Check completed! (Note: Real SMTP checking requires dedicated VPS ports)")
        else:
            st.error("Please paste some emails first.")