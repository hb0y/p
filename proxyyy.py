from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def check_microsoft(email):
    # إعدادات المتصفح المخفي عشان ما يزعجك
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # فك الهاش لو تبي يشتغل في الخلفية
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://login.live.com/oauth20_authorize.srf?client_id=000000004C12AE29&response_type=code&scope=service%3a%3apsrp.v2.microsoft.com%3a%3aDEFAULTPREAUTH&redirect_uri=https%3a%2f%2faccount.microsoft.com%2fauth%2fcomplete-signin-user")
        time.sleep(2) # ننتظر الصفحة تفتح
        
        # نضغط على "Create one!" عشان نروح لصفحة التسجيل
        driver.find_element(By.ID, "signup").click()
        time.sleep(2)
        
        # نكتب الإيميل
        input_box = driver.find_element(By.ID, "MemberName")
        input_box.send_keys(email)
        input_box.send_keys(Keys.ENTER)
        time.sleep(2)
        
        # شيك على رسالة الخطأ
        page_source = driver.page_source
        if "is already taken" in page_source or "Someone already" in page_source:
            print(f"❌ {email} is TAKEN")
        else:
            print(f"✅ {email} is AVAILABLE!")
            
    except Exception as e:
        print(f"⚠️ Error: {e}")
    finally:
        driver.quit()

# جرب هنا
check_microsoft("test_user_99@outlook.com")
