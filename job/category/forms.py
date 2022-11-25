from django import forms
from .models import Jobs
from datetime import datetime

class CreateJob(forms.Form):
    title = forms.CharField(
        label = "Title",
        widget = forms.TextInput(
            attrs = {
                "id": "name",
                "class": "form-control",
                "placeholder": "Title",
                "onfoces": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Title'"
            }
        ),
    )
    work_class = forms.CharField(
        label = "Work class",
        widget = forms.TextInput(
            attrs = {
                "id": "name",
                "class": "form-control",
                "placeholder": "Work class",
                "onfoces": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Work class'"
            }
        ),
    )
    place = forms.CharField(
        label = "Place",
        widget = forms.TextInput(
            attrs = {
                "id": "name",
                "class": "form-control",
                "placeholder": "Place",
                "onfoces": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Place'"
            }
        ),
    )
    work_time = forms.CharField(
        label = "Work time",
        widget = forms.TextInput(
            attrs = {
                "id": "name",
                "class": "form-control",
                "placeholder": "Work time",
                "onfoces": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Work time'"
            }
        ),
    )
    salary = forms.CharField(
        label = "Salary",
        required = False,
        widget = forms.TextInput(
            attrs = {
                "id": "name",
                "class": "form-control",
                "placeholder": "Salary",
                "onfoces": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Salary'"
            }
        ),
    )
    text = forms.CharField(
        label = "Text",
        required = False,
        widget = forms.Textarea(
            attrs = {
                "id" : "name",  
                "rows" : "5",
                "class": "form-control",
                "placeholder": "Text",
                "onfoces": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Text'"
            }
        ),
    )

    def save(self):
        new_job = Jobs(
            title = self.cleaned_data["title"],
            work_class = self.cleaned_data["work_class"],
            place = self.cleaned_data["place"],
            work_time = self.cleaned_data["work_time"],
            salary = self.cleaned_data["salary"],
            text = self.cleaned_data["text"],
            created_date = datetime.now()
        )
        new_job.save()

    class Meta:
        model = Jobs