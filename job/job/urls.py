from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('about_us/', include("about_us.urls")),
    path('blog_home/', include("blog_home.urls")),
    path('users/', include("users.urls")),
    # path('log_in/', include("users.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
