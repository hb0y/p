from psnaw_client import PSNAW
import datetime

# 1. إعداد الاتصال (استبدل الرمز بالرمز الخاص بك)
NPSSO_TOKEN = "ضع_هنا_كود_NPSSO_الخاص_بك"
try:
    client = PSNAW(NPSSO_TOKEN)
except Exception as e:
    print(f"خطأ في الاتصال: {e}")
    exit()

def get_user_info(online_id):
    try:
        # البحث عن المستخدم
        user = client.user(online_id=online_id)
        
        # جلب البيانات
        avatar_url = user.avatar_url
        region = user.region  # يعيد لك الدولة (الريجون)
        languages = user.languages
        
        # جلب حالة الاتصال وآخر ظهور
        presence = user.get_presence()
        last_seen = presence.get("last_available_date")
        
        print(f"\n--- معلومات الآيدي: {online_id} ---")
        print(f"🖼️ رابط الأفتار: {avatar_url}")
        print(f"🌍 ريجون الحساب: {region.upper()}")
        print(f"🗣️ اللغات المسجلة: {', '.join(languages)}")
        
        if last_seen:
            # تحويل الوقت لصيغة مفهومة
            date_obj = datetime.datetime.fromisoformat(last_seen.replace('Z', '+00:00'))
            print(f"🕒 آخر ظهور: {date_obj.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("🕒 آخر ظهور: مخفي أو غير متاح")
            
    except Exception as e:
        print(f"حدث خطأ: تأكد من صحة الآيدي أو إعدادات الخصوصية. \nالتفاصيل: {e}")

# تشغيل الأداة
target_id = input("أدخل آيدي السوني (Online ID): ")
get_user_info(target_id)
