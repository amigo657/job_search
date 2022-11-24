from django.contrib import admin
from category.models import Jobs

class AdminJob(admin.ModelAdmin):
    list_display = ("title", )

admin.site.register(Jobs, AdminJob)