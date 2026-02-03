from psnaw_client import PSNAW
import datetime

# --- إعدادات الأداة ---
# يجب وضع الـ NPSSO الخاص بك هنا لكي تعمل الأداة
NPSSO = "ضع_هنا_كود_NPSSO_الخاص_بك" 

def run_tool():
    try:
        client = PSNAW(NPSSO)
        print("✅ تم الاتصال بخوادم سوني بنجاح.")
        
        target_id = input("\n[?] أدخل آيدي الشخص اللي تبي تسحب معلوماته: ")
        user = client.user(online_id=target_id)
        
        # سحب البيانات
        presence = user.get_presence()
        last_seen = presence.get("last_available_date")
        
        print("\n" + "="*40)
        print(f"🆔 الآيدي: {user.online_id}")
        print(f"🖼️ رابط الأفتار: {user.avatar_url}")
        print(f"🌍 ريجون الحساب: {user.region.upper()}")
        print(f"🇸🇦 اللغة: {user.languages}")
        
        if last_seen:
            # تنسيق الوقت
            date_obj = datetime.datetime.fromisoformat(last_seen.replace('Z', '+00:00'))
            print(f"🕒 آخر ظهور: {date_obj.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("🕒 آخر ظهور: مخفي من إعدادات الخصوصية")
