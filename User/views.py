from django.shortcuts import render, redirect, render_to_response, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from User.form import  CreationForm
from django.views.decorators.csrf import csrf_exempt
from django.conf  import settings
# from django.contrib import messages
from django.core.mail import send_mail
from django.utils.timezone import now
import os
# Create your views here.


class user_login_view(LoginView):
    template_name = 'User/login.html'
    redirect_authenticated_user = True


class user_logout_view(LogoutView):
    template_name = 'User/login.html'
    next_page = '/login'


@csrf_exempt
def user_adduser_view(request):
    template_name = 'User/sign-up.html'
    context = {
        "add_form": CreationForm(),
    }
    if request.method == "GET":
        return render_to_response(template_name, context)
    if request.method == "POST":
        add_form = CreationForm(request.POST)
        if add_form.is_valid():
            if add_form.clean_password2():
                add_form.save(commit=True)
        return redirect('/login')


