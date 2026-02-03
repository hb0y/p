# ملاحظة: هذا مثال توضيحي للمنطق البرمجي
from psnaw_client import PSNAW

# تحتاج لرمز تسجيل الدخول الخاص بك للوصول للبيانات العامة
npsso_token = "ضع_هنا_الرمز_الخاص_بك"
client = PSNAW(npsso_token)

# البحث عن آيدي معين
user = client.user(online_id="ID_HERE")

print(f"اسم المستخدم: {user.online_id}")
print(f"المستوى (Level): {user.trophy_summary.level}")
print(f"الحالة: {user.is_online}")
