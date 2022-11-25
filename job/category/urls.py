from django.urls import path
from category.views import jobs, create_job

urlpatterns = [
    path("", jobs, name = 'jobs'),
    path("create/", create_job, name = "create_job")
]