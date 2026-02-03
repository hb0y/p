import streamlit as st
from psnaw_client import PSNAW
import datetime

st.set_page_config(page_title="PSN Tool", page_icon="🎮")
st.title("🎮 أداة فحص آيديات سوني")

npsso = st.text_input("كود NPSSO:", type="password")
target_id = st.text_input("الآيدي المستهدف:")

if st.button("بدء السحب"):
    if npsso and target_id:
        try:
            client = PSNAW(npsso)
            user = client.user(online_id=target_id)
            
            # جلب البيانات
            presence = user.get_presence()
            last_seen = presence.get("last_available_date")
            
            st.success(f"تم العثور على الحساب: {target_id}")
            
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(user.avatar_url, width=150)
            with col2:
                st.write(f"🌍 **الريجون:** {user.region.upper()}")
                if last_seen:
                    dt = datetime.datetime.fromisoformat(last_seen.replace('Z', '+00:00'))
                    st.write(f"🕒 **آخر ظهور:** {dt.strftime('%Y-%m-%d %H:%M')}")
                else:
                    st.write("🕒 **آخر ظهور:** مخفي")
        except Exception as e:
            st.error("تأكد من صحة الـ NPSSO أو الآيدي.")
    else:
        st.warning("يرجى إدخال البيانات.")
