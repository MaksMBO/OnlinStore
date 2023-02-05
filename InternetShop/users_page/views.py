import base64
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.shortcuts import redirect

from .forms import UserRegistrationForm, UserEmailLogin, UserPhoneLogin

User = get_user_model()


class Error():
    errors = []
    temp_error = []


class Home(Error, ListView):

    def get(self, request):
        user_register = UserRegistrationForm()
        user_email_login = UserEmailLogin()
        user_phone_login = UserPhoneLogin()
        
        self.temp_error.clear()
        self.temp_error = self.errors.copy()
        self.errors.clear()
        
        return render(request, 'users_page/authorization.html', context={
            'register_form': user_register, 'email_login_form': user_email_login,
            'phone_login_form': user_phone_login, "errors": self.temp_error})


class Register(Error, ListView):

    def post(self, request, *args, **kwargs):
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.cleaned_data
            
            email = new_user['email']
            if not User.objects.filter(email=email):
                self.errors = []
                first_name = new_user['first_name']
                last_name = new_user['last_name']
                phone = new_user['phone'].as_e164
                password = base64.b64encode(
                    str(new_user['password']).encode("utf-8")).decode("utf-8")

                user = User.objects.create(first_name=first_name, last_name=last_name,
                                           phone=phone, email=email, password=password, username=last_name+first_name)
                user.save()
            else:
                self.errors.append("Користувач з таким email вже існує")
        else:
            self.errors.append("Користувач з таким телефоном вже створений")

        return redirect(request.META.get('HTTP_REFERER'))


class LoginPhone(Error, ListView):

    def post(self, request, *args, **kwargs):
        phone_form = UserPhoneLogin(request.POST) 
        
        if phone_form.is_valid():
            user = phone_form.cleaned_data
            phone = user['phone']
            password = base64.b64encode(
                str(user['password']).encode("utf-8")).decode("utf-8")
            user_auth = None

            try:
                user_auth = User.objects.get(phone=phone, password=password)
                self.errors = []
            except (AttributeError, User.DoesNotExist):
                self.errors.append("Такого користувача не існує")

            if user_auth is not None:
                login(request, user_auth)
        else:
            self.errors.append("Такого користувача не існує")
        
        return redirect(request.META.get('HTTP_REFERER'))


class LoginEmail(Error, ListView):

    def post(self, request):
        email_form = UserEmailLogin(request.POST)
        
        if email_form.is_valid():
            user = email_form.cleaned_data
            email = user['email']
            password = base64.b64encode(
                str(user['password']).encode("utf-8")).decode("utf-8")
            user_auth = None

            try:
                user_auth = User.objects.get(email=email, password=password)
                self.errors = []
            except (AttributeError, User.DoesNotExist):
                self.errors.append("Такого користувача не існує")

            if user_auth is not None:
                login(request, user_auth)
        else: 
            self.errors.append("Такого користувача не існує")

        return redirect(request.META.get('HTTP_REFERER'))
