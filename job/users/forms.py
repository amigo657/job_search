from django import forms

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