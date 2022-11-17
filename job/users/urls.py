from django.urls import path
from users.views import sign_in, log_in, log_out

urlpatterns =[
    path("sign_up/", sign_in, name = "sign_in"),
    path("log_in/", log_in, name = 'login'),
    path("log_out/", log_out, name = "log_out"),
]