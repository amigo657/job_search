from django.contrib import admin
from users.models import User

class AdminUser(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ("username",)
=======
    list_display = ("username", "is_agree")
>>>>>>> 8bbdaef (login page)

# Register your models here.
admin.site.register(User, AdminUser)