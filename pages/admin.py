
from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # نمایش این فیلدها در لیست
    search_fields = ('name', 'email')  # قابلیت جستجو بر اساس نام و ایمیل