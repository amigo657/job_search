from django.contrib import admin
from users.models import User

class AdminUser(admin.ModelAdmin):
    list_display = ("username", "is_agree")

# Register your models here.
admin.site.register(User, AdminUser)