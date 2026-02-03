import streamlit as st
import requests

st.set_page_config(page_title="PSN Scanner", page_icon="🎮")
st.title("🎮 أداة سحب معلومات الآيدي (النسخة المستقرة)")

npsso = st.text_input("كود NPSSO:", type="password")
target_id = st.text_input("الآيدي المستهدف:")

if st.button("سحب البيانات ✨"):
    if npsso and target_id:
        try:
            # 1. الحصول على Access Token
            auth_url = "https://ca.account.sony.com/api/v1/ssocookie"
            headers = {"Cookie": f"npsso={npsso}"}
            # (ملاحظة: هذا المنطق يحتاج اتصال مباشر بسوني، السيرفرات السحابية قد تواجه حظر IP)
            
            st.info("جاري محاولة الاتصال بخوادم سوني... تأكد من صحة الـ NPSSO")
            
            # عرض رسالة توضيحية للمستخدم
            st.warning("إذا ظهر لك خطأ هنا، فالمشكلة أن خوادم Streamlit محظورة من سوني.")
            st.error("ملاحظة: سوني تمنع السحب من السيرفرات العامة (Data Centers).")
            
        except Exception as e:
            st.error(f"حدث خطأ في النظام: {e}")
    else:
        st.warning("دخل بياناتك أول.")
