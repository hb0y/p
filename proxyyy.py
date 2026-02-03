import os

# محاولة تثبيت المكتبة تلقائياً إذا كانت ناقصة
try:
    from psnaw_client import PSNAW
except ImportError:
    print("جاري تثبيت المكتبات المطلوبة... انتظر لحظة")
    os.system('pip install psnaw_client')
    from psnaw_client import PSNAW

import datetime

def s_tool():
    print("--- PSN ID SCANNER ---")
    npsso = input("أدخل كود NPSSO: ")
    target = input("أدخل الآيدي المستهدف: ")

    try:
        client = PSNAW(npsso)
        user = client.user(online_id=target)
        presence = user.get_presence()
        
        print("\n" + "="*30)
        print(f"ID: {user.online_id}")
        print(f"Region: {user.region.upper()}")
        print(f"Avatar: {user.avatar_url}")
        
        last_seen = presence.get("last_available_date")
        if last_seen:
            dt = datetime.datetime.fromisoformat(last_seen.replace('Z', '+00:00'))
            print(f"Last Seen: {dt.strftime('%Y-%m-%d %H:%M')}")
        else:
            print("Last Seen: Private")
        print("="*30)
    except Exception as e:
        print(f"خطأ: {e}")

if __name__ == "__main__":
    s_tool()
    input("\nاضغط Enter للخروج...")
