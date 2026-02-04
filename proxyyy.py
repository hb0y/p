import streamlit as st
import requests

st.set_page_config(page_title="PS3 Avatar Tool", page_icon="🎮")

st.title("PS3 Avatars Manager 🎮")
st.markdown("---")

# دالة تحويل الـ NPSSO إلى Access Token
def get_access_token(npsso_token):
    try:
        # رابط الحصول على كود التصديق
        auth_url = "https://ca.account.sony.com/api/v1/oauth/authorize"
        params = {
            "access_type": "offline",
            "client_id": "09515159-7237-43f0-9f0d-033593f1ee27", # Client ID رسمي لتطبيقات سوني
            "response_type": "code",
            "scope": "psn:mobile.v2.core psn:client.attributes",
            "redirect_uri": "com.scee.psxandroid.sceplogin://redirect",
        }
        headers = {"Cookie": f"npsso={npsso_token}"}
        
        # 1. طلب كود التصديق
        res = requests.get(auth_url, params=params, headers=headers, allow_redirects=False)
        auth_code = res.headers['Location'].split("code=")[1].split("&")[0]
        
        # 2. تبديل الكود بالتوكن النهائي
        token_url = "https://ca.account.sony.com/api/v1/oauth/token"
        data = {
            "code": auth_code,
            "redirect
