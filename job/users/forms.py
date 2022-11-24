from django import forms
from django.contrib.auth.models import User
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        label = "User name",
        widget = forms.TextInput(
            attrs = {
                "id": "name",
                "class": "form-control",
                "placeholder": "User name",
                "onfoces": "this.placeholder = ''",
                "onblur": "this.placeholder = 'User name'"
            }
        ),
    )
    password = forms.CharField(
        label = "Password",
        widget=forms.PasswordInput(
            attrs = {
                "id": "password",
                "class": "form-control",
                "placeholder": "Password",
                "onfoces": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Password'"
            }
        ),
    )

    # username = forms.CharField()
    # password = forms.CharField(widget = forms.PasswordInput())

class SignInForm(forms.Form):
    first_name = forms.CharField(
        max_length = 10,
        widget = forms.TextInput(
            attrs = {
                "id": "first_name",
                "class": "form-control",
                "placeholder": "First name",
                "onfoces": "this.placeholder = ''",
                "onblur": "this.placeholder = 'First name'"
            }
        ),
    )
    username = forms.CharField(
        max_length = 10,
        widget = forms.TextInput(
            attrs = {
                "id": "name",
                "class": "form-control",
                "placeholder": "User name",
                "onfoces": "this.placeholder = ''",
                "onblur": "this.placeholder = 'User name'"
            }
        ),
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs = {
                "id": "email",
                "class": "form-control",
                "placeholder": "Email",
                "onfoces": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Email'"
            }
        ),
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "id": "name",
                "class": "form-control",
                "placeholder": "Password",
                "onfoces": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Password'"
            }
        ),
    )
    repeat_password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "id": "name",
                "class": "form-control",
                "placeholder": "Repaet password",
                "onfoces": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Repaet password'"
            }
        ),
    )
    is_agree = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs = {
                "id": "is_agree",
                "class": "form-control",
            }
        ),
    )

    def check_password(self):
        cd = self.cleaned_data
        if cd['password'] == cd['repeat_password']:
            return True

    def save(self):
        new_user = User(
            username = self.cleaned_data["username"],
            email = self.cleaned_data["email"],
            first_name = self.cleaned_data["first_name"],
            password = self.cleaned_data["password"],
        )
        new_user.save()

