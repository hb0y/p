import streamlit as st
from psnaw_client import PSNAW
import datetime

# إعداد الصفحة بثيم أسود
st.set_page_config(page_title="PSN Hunter", page_icon="🕵️‍♂️", layout="centered")

# CSS لتعديل الشكل وتوسيط المحتوى
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stTextInput { text-align: center; }
    .block-container { padding-top: 2rem; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🕵️‍♂️ PSN Info Scanner")
st.write("ادخل البيانات لسحب تفاصيل الحساب")

# الخيارات في المنتصف
npsso = st.text_input("كود NPSSO الخاص بك:", type="password")
target_id = st.text_input("اكتب آيدي السوني (Online ID):")

if st.button("فحص الحساب 🔍"):
    if npsso and target_id:
        try:
            client = PSNAW(npsso)
            user = client.user(online_id=target_id)
            
            # سحب البيانات
            presence = user.get_presence()
            trophies = user.trophy_summary()
            
            st.divider()
            
            # عرض الغلاف (Banner/Cover) إذا وجد
            # ملاحظة: بعض الحسابات لا تملك غلاف عام
            
            # عرض الصورة الشخصية والمعلومات
            st.image(user.avatar_url, width=150)
            st.subheader(f"ID: {user.online_id}")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("الريجون", user.region.upper())
            with col2:
                st.metric("المستوى", trophies.level)
            with col3:
                st.metric("التروفيز", trophies.earned_trophies)

            # تفاصيل التروفيز الدقيقة
            st.write(f"🏆 **البلاتنيوم:** {trophies.platinum} | **الذهبي:** {trophies.gold}")
            
            # تاريخ الدخول
            last_seen = presence.get("last_available_date")
            if last_seen:
                dt = datetime.datetime.fromisoformat(last_seen.replace('Z', '+00:00'))
                st.info(f"🕒 آخر ظهور: {dt.strftime('%Y-%m-%d %H:%M')}")
            else:
                st.warning("🕒 آخر ظهور: مخفي")

        except Exception as e:
            st.error("خطأ: تأكد من الـ NPSSO أو أن الآيدي صحيح")
    else:
        st.warning("يرجى إكمال الخانات")
