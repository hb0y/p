import streamlit as st
from psnaw_client import PSNAW
import datetime

# إعداد واجهة الموقع
st.set_page_config(page_title="PSN Scanner", page_icon="🎮")
st.title("🎮 سحب معلومات آيدي سوني")

# المدخلات
npsso = st.text_input("ضع كود NPSSO هنا:", type="password")
target_id = st.text_input("أدخل الآيدي (ID) المطلوب:")

if st.button("اسحب البيانات 🚀"):
    if npsso and target_id:
        try:
            # الاتصال بسوني
            client = PSNAW(npsso)
            user = client.user(online_id=target_id)
            
            # جلب الحالة وآخر ظهور
            presence = user.get_presence()
            last_seen = presence.get("last_available_date")
            
            st.success(f"تم العثور على {target_id}")
            st.divider()

            # عرض البيانات
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(user.avatar_url, width=150)
            
            with col2:
                st.write(f"**الريجون:** {user.region.upper()}")
                st.write(f"**اللغة:** {', '.join(user.languages)}")
                
                if last_seen:
                    dt = datetime.datetime.fromisoformat(last_seen.replace('Z', '+00:00'))
                    st.write(f"**آخر ظهور:** {dt.strftime('%Y-%m-%d %H:%M')}")
                else:
                    st.write("**آخر ظهور:** مخفي")
                    
        except Exception as e:
            st.error("فيه مشكلة! تأكد إن الـ NPSSO حقك شغال والآيدي صح.")
    else:
        st.warning("عبّ البيانات أول يا بطل.")
