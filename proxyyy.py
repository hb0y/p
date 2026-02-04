import streamlit as st
import requests

st.set_page_config(page_title="PS3 Avatar Tool", page_icon="🎮")

st.title("PS3 Avatars Manager 🎮")
st.markdown("---")

# دالة تحويل الـ NPSSO إلى Access Token
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
        
        # طلب كود التصديق
        res = requests.get(auth_url, params=params, headers=headers, allow_redirects=False)
        if 'Location' not in res.headers:
            st.error("خطأ: كود NPSSO غير صحيح أو منتهي الصلاحية.")
            return None
            
        auth_code = res.headers['Location'].split("code=")[1].split("&")[0]
        
        # تبديل الكود بالتوكن النهائي
        token_url = "https://ca.account.sony.com/api/v1/oauth/token"
        data = {
            "code": auth_code,
            "redirect_uri": "com.scee.psxandroid.sceplogin://redirect",
            "grant_type": "authorization_code",
            "token_format": "jwt",
        }
        auth_headers = {"Authorization": "Basic MDk1MTUxNTktNzIzNy00M2YwLTlmMGQtMDMzNTkzZjFlZTI3OmV4cGloV1VvS0pXbkpockt="}
        
        token_res = requests.post(token_url, data=data, headers=auth_headers)
        return token_res.json().get("access_token")
    except Exception as e:
        st.error(f"حدث خطأ أثناء الاتصال بسوني: {e}")
        return None

# واجهة المستخدم
npsso_input = st.text_input("Enter NPSSO Token", type="password")
product_id = st.text_input("Enter Avatar Product ID", value="EP4491-CUSA05486_00-AVATAR0000000011")

if st.button("Add to Cart"):
    if npsso_input and product_id:
        with st.spinner('جاري العمل...'):
            final_token = get_access_token(npsso_input)
            
            if final_token:
                cart_url = "https://cart.playstation.com/api/v1/users/me/cart/items"
                headers = {
                    "Authorization": f"Bearer {final_token}",
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                }
                payload = {"id": product_id}
                
                try:
                    res = requests.post(cart_url, json=payload, headers=headers)
                    if res.status_code in [200, 201]:
                        st.success("✅ تمت الإضافة بنجاح! شيك على سلة حسابك.")
                    else:
                        st.error(f"سوني رفضت الطلب. كود الخطأ: {res.status_code}")
                        st.write(res.json())
                except Exception as e:
                    st.error(f"فشل الاتصال بخادم السلة: {e}")
    else:
        st.warning("عبّ البيانات أول يا بطل")
