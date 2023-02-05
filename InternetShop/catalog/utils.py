from django.shortcuts import render

from users_page.forms import UserRegistrationForm, UserEmailLogin, UserPhoneLogin

class Notifications:
    errors = []
    temp_error = []
    success = []
    temp_success = []
    
    def add_to_temp(self, list_name, temp_name):
        temp_name.clear()
        temp_name = list_name.copy()
        list_name.clear()
        return temp_name
    
    
class CatalogMixin(Notifications):
    
    def renderPage(self, request, html):
        user_register = UserRegistrationForm()
        user_email_login = UserEmailLogin()
        user_phone_login = UserPhoneLogin()
        
        self.temp_error = self.add_to_temp(self.errors, self.temp_error)
        self.temp_success = self.add_to_temp(self.success, self.temp_success)
        
        return render(request, html, context={
            'register_form': user_register, 'email_login_form': user_email_login,
            'phone_login_form': user_phone_login, 'errors': self.temp_error,
            'success':self.temp_success})
        