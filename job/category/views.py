from django.shortcuts import render
from category.models import Jobs

def jobs(request):
    job = {"job" : Jobs.objects.all()}
    return render(request, "category.html", job)