from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage # اضافه کردن مدل ContactMessage
from django.shortcuts import redirect

@csrf_exempt  # این دکمه برای تست است، در محیط تولید از آن استفاده نکنید
def home(request):
    success_message = False  # متغیر برای نشان دادن موفقیت

    if request.method == 'POST':
        # دریافت داده‌های فرم
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # ذخیره پیام در پایگاه داده
        contact_message = ContactMessage(name=name, email=email, message=message)
        contact_message.save()  

        # ارسال ایمیل به کاربر
        subject = 'Thank you for contacting me!'
        body =f"""
        Dear {name},

        Thank you for reaching out and taking the time to contact me. I have received your message and will review it carefully. I will get back to you as soon as possible.

        If you have any further questions or need additional information, please feel free to reply to this email.

        Best regards,  
        {name}  
        {email}

        """

        send_mail(subject, body, settings.EMAIL_HOST_USER, [email])

        success_message = True  # پیام با موفقیت ارسال شد
        return redirect('home')

    return render(request, 'index.html', {'success_message': success_message})