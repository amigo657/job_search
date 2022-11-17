from urllib.parse import urlparse
from django.urls import path
from about_us.views import aboutus_page

urlpatterns = [
    path("", aboutus_page, name = "about_us")
]