import streamlit as st
import requests

st.set_page_config(page_title="PS3 Avatar Store", page_icon="🎮", layout="wide")

# --- قاعدة بيانات الافتارات (تقدر تزيد عليها بنفس الترتيب) ---
AVATAR_LIBRARY = [
    {"name": "Monreve Avatar II", "id": "EP4491-CUSA05486_00-AVATAR0000000011", "price": "1.49$", "region": "SA/EU"},
    {"name": "God of War: Kratos", "id": "UP9000-NPUA80491_00-AVATAR0000000001", "price": "0.49$", "region": "US"},
    {"name": "Uncharted: Nathan Drake", "id": "UP0001-NPUA80033_00-AVATAR0000000001", "price": "0.49$", "region": "US"},
    {"name": "The Last of Us: Joel", "id": "UP9000-NPUA80960_00-AVATAR0000000002", "price": "0.49$", "region": "US"},
    {"name": "Sly Cooper", "id": "EP9000-NPEA00338_00-AVATAR0000000001", "price": "0.25$", "region": "SA/EU"}
]

# --- دالة تحويل NPSSO إلى Access Token ---
def get_access_token(npsso_token):
    try:
        auth_url = "https://ca.account.sony.com/api/v1/oauth/authorize"
        params = {
            "access_type": "offline",
            "client_id": "09515159-7237-43f0-9f0d-033593f1ee27",
            "response_type": "code",
            "scope": "psn:mobile.v2.core psn:client.attributes",
            "redirect_uri": "com.scee.psxandroid.sceplogin://redirect",
        }
        headers = {"Cookie": f"npsso={npsso_token}"}
        res = requests.get(auth_url, params=params, headers=headers, allow_redirects=False)
        if 'Location' not in res.headers:
            return None
        auth_code = res.headers['Location'].split("code=")[1].split("&")[0]
        
        token_url = "https://ca.account.sony.com/api/v1/oauth/token"
        data = {"code": auth_code, "redirect_uri": "com.scee.psxandroid.sceplogin://redirect", "grant_type": "authorization_code", "token_format": "jwt"}
        auth_headers = {"Authorization": "Basic MDk1MTUxNTktNzIzNy00M2YwLTlmMGQtMDMzNTkzZjFlZTI3OmV4cGloV1VvS0pXbkpockt="}
        token_res = requests.post(token_url, data=data, headers=auth_headers)
        return token_res.json().get("access_token")
    except:
        return None

# --- الواجهة ---
st.title("🎮 متجر افتارات سوني 3")
st.info("سجل دخول في موقع سوني وهات كود الـ NPSSO عشان تقدر تضيف للسلة.")

npsso = st.text_input("أدخل كود الـ NPSSO هنا:", type="password")

st.subheader("🛍️ مكتبة الافتارات المتوفرة")
cols = st.columns(3) # عرض الافتارات في 3 أعمدة

for i, item in enumerate(AVATAR_LIBRARY):
    with cols[i % 3]:
        st.markdown(f"### {item['name']}")
        st.code(item['id'], language="text")
        st.write(f"**المنطقة:** {item['region']} | **السعر:** {item['price']}")
        
        # زر الإضافة لكل افتار
        if st.button(f"أضف للسلة 🛒", key=f"btn_{i}"):
            if not npsso:
                st.warning("لازم تحط كود الـ NPSSO أولاً!")
            else:
                with st.spinner('جاري الإضافة...'):
                    token = get_access_token(npsso)
                    if token:
                        cart_url = "https://cart.playstation.com/api/v1/users/me/cart/items"
                        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
                        res = requests.post(cart_url, json={"id": item['id']}, headers=headers)
                        
                        if res.status_code in [200, 201]:
                            st.success(f"✅ تم إضافة {item['name']} للسلة!")
                        else:
                            st.error(f"فشل: ريجون الحساب قد لا يطابق الافتار.")
                    else:
                        st.error("كود الـ NPSSO غير صحيح أو انتهت صلاحيته.")

st.markdown("---")
st.caption("تطوير أداة سوني 3 - تأكد من تطابق ريجون حسابك مع الافتار المختار.")
