import streamlit as st
import requests

st.title("PS3 Avatars Manager 🎮")

# مدخلات المستخدم
npsso_token = st.text_input("Enter NPSSO Token", type="password")
product_id = st.text_input("Enter Avatar Product ID", placeholder="e.g. UP9000-NPUA80491_00-AVATAR0000000001")

if st.button("Add to Cart"):
    if npsso_token and product_id:
        # ملاحظة: هنا نحتاج تحويل NPSSO لـ Access Token (سأعطيك الطريقة لاحقاً)
        # للتبسيط الآن سنفترض أنك وضعت الـ Access Token مباشرة
        
        url = "https://cart.playstation.com/api/v1/users/me/cart/items"
        headers = {
            "Authorization": f"Bearer {npsso_token}", # التوكن النهائي
            "Content-Type": "application/json"
        }
        data = {"id": product_id}
        
        try:
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 201 or response.status_code == 200:
                st.success("✅ تم إضافة الافتار للسلة بنجاح!")
            else:
                st.error(f"❌ خطأ من سوني: {response.status_code}")
                st.write(response.text)
        except Exception as e:
            st.error(f"حدث خطأ تقني: {e}")
    else:
        st.warning("الرجاء إدخال التوكن و ID الافتار")
