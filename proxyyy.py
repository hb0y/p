const axios = require('axios');

// دالة إضافة الافتار للسلة
async function addToCart(accessToken, productId) {
    // رابط سوني لإضافة المنتجات للسلة
    const url = "https://cart.playstation.com/api/v1/users/me/cart/items";

    // البيانات المطلوبة: الـ ID الخاص بالافتار
    const data = {
        "id": productId
    };

    const config = {
        headers: {
            'Authorization': `Bearer ${accessToken}`, // التوكن هنا
            'Content-Type': 'application/json',
            'Accept-Language': 'en-US', // مهم لتحديد الريجون
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
        }
    };

    try {
        const response = await axios.post(url, data, config);
        console.log("✅ تمت الإضافة بنجاح!");
        console.log("تفاصيل السلة الحالية:", response.data);
    } catch (error) {
        console.error("❌ فشلت العملية:");
        if (error.response) {
            console.error("السبب:", error.response.data.error.message);
        } else {
            console.error(error.message);
        }
    }
}

// --- مثال للاختبار ---
// التوكن (يجب أن يكون صالحاً وغير منتهي)
const myToken = "اكتب_هنا_التوكن_الخاص_بالحساب"; 

// الـ Product ID الخاص بالافتار (مثال لافتار ريجون أمريكي)
const avatarID = "UP9000-NPUA80491_00-AVATAR0000000001"; 

addToCart(myToken, avatarID);
