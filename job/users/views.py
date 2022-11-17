from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignInForm
from django.shortcuts import render, redirect


def sign_in(request):
    user_form = {"user_form" : SignInForm()}
    if request.method == "POST":
        user_form = SignInForm(request.POST)
        if user_form.is_valid():
            print(user_form.is_valid())
            # context = {"login_form": LoginForm()}
            return redirect('/users/log_in/')
            # return render(request, "log_in.html", context)
        else:
            # return HttpResponseRedirect("/users/log_in/")
            return render(request, "sign_in.html", user_form)
    else:
        return render(request, "sign_in.html", user_form)


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