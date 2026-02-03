import streamlit as st
from psnaw_client import PSNAW
import datetime

st.set_page_config(page_title="PSN ID Scanner", page_icon="🎮")

st.title("🎮 سحب معلومات آيدي سوني")

# مدخلات الأداة
npsso_token = st.text_input("أدخل كود NPSSO الخاص بك:", type="password")
target_id = st.text_input("أدخل الآيدي المستهدف (Online ID):")

if st.button("بدء السحب 🚀"):
    if not npsso_token or not target_id:
        st.error("⚠️ يرجى إدخال الكود والآيدي أولاً")
    else:
        try:
            client = PSNAW(npsso_token)
            user = client.user(online_id=target_id)
            
            # جلب البيانات
            presence = user.get_presence()
            last_seen = presence.get("last_available_date")
            
            st.divider()
            
            # عرض النتائج
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(user.avatar_url, caption="Avatar", width=150)
                
            with col2:
                st.subheader(f"🆔 {user.online_id}")
                st.write(f"🌍 **الريجون:** {user.region.upper()}")
                st.write(f"🗣️ **اللغة:** {', '.join(user.languages)}")
                
                if last_seen:
                    date_obj = datetime.datetime.fromisoformat(last_seen.replace('Z', '+00:00'))
                    st.write(f"🕒 **آخر ظهور:** {date_obj.strftime('%Y-%m-%d %H:%M:%S')}")
                else:
                    st.write("🕒 **آخر ظهور:** مخفي من إعدادات الخصوصية")
                    
        except Exception as e:
            st.error(f"❌ حدث خطأ: تأكد من الكود أو أن الآيدي صحيح.")
            st.info("تأكد أن حسابك مسجل دخول في المتصفح وجبت الـ NPSSO صح.")
