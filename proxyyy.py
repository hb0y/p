import requests

def add_avatar_to_cart(npsso_token, product_id):
    # تحويل الـ NPSSO إلى Access Token (هذه الخطوة ضرورية لأن سوني لا تقبل الـ NPSSO مباشرة في السلة)
    # ملاحظة: تحتاج سكربت المصادقة لجلب الـ Access Token أولاً
    access_token = "ضع_هنا_الـ_Access_Token" 
    
    url = "https://cart.playstation.com/api/v1/users/me/cart/items"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    
    data = {
        "id": product_id
    }

    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 201 or response.status_code == 200:
        print("✅ تم إضافة الافتار للسلة بنجاح!")
    else:
        print(f"❌ فشل: {response.status_code}")
        print(response.text)

# تجربة
# add_avatar_to_cart("TOKEN_HERE", "UP9000-NPUA80491_00-AVATAR0000000001")
