<<<<<<< HEAD
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignInForm
from django.shortcuts import render, redirect


def sign_in(request):
    context = {"user_form" : SignInForm()}
    if request.method == "POST":
        user_form = SignInForm(request.POST)
        if user_form.is_valid():
            if user_form.check_password() == True:
                user_form.save()
                return redirect('/users/log_in/')
            else:
                context.update(user_form = user_form)
                return render(request, "sign_in.html", context)
            # context = {"login_form": LoginForm()}
            # return render(request, "log_in.html", context)
        else:
            context.update(user_form = user_form)
            return render(request, "sign_in.html", context)
    return render(request, "sign_in.html", context)

def log_in(request):
    context = {"login_form": LoginForm()}
=======
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.shortcuts import render


def sign_in(request):
    return render(request, "sign_in.html", {})

# def log_in(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             print(user)
#             print(type(user))
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return render(request, "home.html", {})
#     else:
#         form = LoginForm()
#     return render(request, 'log_in.html', {'form': form})

def log_in(request):
    context = {"login_form": LoginForm()}
    print(context)
>>>>>>> 8bbdaef (login page)
    if request.method == "POST":
        user_form = LoginForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            login(request, user)
            return render(request, 'home.html')
        else:
            ...
        context.update(login_form=user_form)
    return render(request, "log_in.html", context)

def log_out(request):
    logout(request)
    return render(request, "home.html", {})