from django.shortcuts import render, redirect
from category.models import Jobs
from category.forms import CreateJob

def jobs(request):
    job = {"job" : Jobs.objects.all()}
    print(job)
    return render(request, "category.html", job)

def create_job(request):
    context = {"create_job" : CreateJob}
    if request.method == "POST":
        fields = CreateJob(request.POST)
        print(fields)
        if fields.is_valid():
            fields.save()
            return redirect("/category/")
    return render(request, "create_job.html", context)