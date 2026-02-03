import streamlit as st
from psnaw_client import PSNAW
import datetime

# إعداد واجهة الصفحة
st.set_page_config(page_title="PSN Scanner", page_icon="🎮")

st.title("🎮 أداة سحب معلومات الآيدي")

# مدخلات المستخدم
npsso = st.text_input("كود NPSSO:", type="password")
target_id = st.text_input("الآيدي (Online ID):")

if st.button("سحب البيانات ✨"):
    if npsso and target_id:
        try:
            # محاولة الاتصال
            client = PSNAW(npsso)
            user = client.user(online_id=target_id)
            
            # جلب البيانات
            presence = user.get_presence()
            last_seen = presence.get("last_available_date")
            
            st.divider()
            
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(user.avatar_url, width=150)
            
            with col2:
                st.subheader(f"آيدي: {user.online_id}")
                st.write(f"🌍 **الريجون:** {user.region.upper()}")
                st.write(f"🗣️ **اللغات:** {', '.join(user.languages)}")
                
                if last_seen:
                    dt = datetime.datetime.fromisoformat(last_seen.replace('Z', '+00:00'))
                    st.write(f"🕒 **آخر ظهور:** {dt.strftime('%Y-%m-%d %H:%M')}")
                else:
                    st.write("🕒 **آخر ظهور:** مخفي")
                    
        except Exception as e:
            st.error("حدث خطأ! تأكد من كود NPSSO أو الآيدي.")
    else:
        st.warning("يرجى إدخال كافة البيانات.")
