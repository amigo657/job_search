from django.urls import path
from category.views import jobs

urlpatterns = [
    path("", jobs, name = 'jobs')
]