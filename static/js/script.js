// script.js

// تابعی برای نمایش یک پیام خوش آمدگویی
function showWelcomeMessage() {
    alert("Welcome to my portfolio website!");
}

// تابعی برای تغییر رنگ پس‌زمینه
function changeBackgroundColor(color) {
    document.body.style.backgroundColor = color;
}

// افزودن رویداد کلیک به دکمه "Contact Me"
document.addEventListener("DOMContentLoaded", function() {
    const contactButton = document.querySelector(".btn-primary");
    if (contactButton) {
        contactButton.addEventListener("click", function() {
            showWelcomeMessage();
            changeBackgroundColor("#f0f8ff"); // تغییر رنگ پس‌زمینه به آبی روشن
        });
    }
});