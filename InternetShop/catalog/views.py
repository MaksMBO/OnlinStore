from django.shortcuts import render
from django.views.generic.list import ListView

from users_page.forms import UserRegistrationForm, UserEmailLogin, UserPhoneLogin

class Error():
    errors = []
    temp_error = []
    
    
class Catalog(Error, ListView):
    
    def get(self, request):
        user_register = UserRegistrationForm()
        user_email_login = UserEmailLogin()
        user_phone_login = UserPhoneLogin()
        
        self.temp_error.clear()
        self.temp_error = self.errors.copy()
        self.errors.clear()
        
        return render(request, 'catalog/catalog.html', context={
            'register_form': user_register, 'email_login_form': user_email_login,
            'phone_login_form': user_phone_login, "errors": self.temp_error})
        
class AboutProduct(Error, ListView):
    def get(self, request):
        user_register = UserRegistrationForm()
        user_email_login = UserEmailLogin()
        user_phone_login = UserPhoneLogin()
        
        self.temp_error.clear()
        self.temp_error = self.errors.copy()
        self.errors.clear()
        
        return render(request, 'catalog/aboutProduct.html', context={
            'register_form': user_register, 'email_login_form': user_email_login,
            'phone_login_form': user_phone_login, "errors": self.temp_error})
        
        
class ProductComparison(Error, ListView):
    def get(self, request):
        user_register = UserRegistrationForm()
        user_email_login = UserEmailLogin()
        user_phone_login = UserPhoneLogin()
        
        self.temp_error.clear()
        self.temp_error = self.errors.copy()
        self.errors.clear()
        
        return render(request, 'catalog/productComparison.html', context={
            'register_form': user_register, 'email_login_form': user_email_login,
            'phone_login_form': user_phone_login, "errors": self.temp_error})
    