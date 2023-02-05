from django.shortcuts import render

from users_page.forms import UserRegistrationForm, UserEmailLogin, UserPhoneLogin
from users_page.views import Error
    
    
class CatalogMixin(Error):
    
    def renderPage(self, request, html):
        user_register = UserRegistrationForm()
        user_email_login = UserEmailLogin()
        user_phone_login = UserPhoneLogin()
        
        self.temp_error.clear()
        self.temp_error = self.errors.copy()
        self.errors.clear()
        
        return render(request, html, context={
            'register_form': user_register, 'email_login_form': user_email_login,
            'phone_login_form': user_phone_login, "errors": self.temp_error})
        