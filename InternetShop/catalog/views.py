from django.shortcuts import render
from django.views.generic.list import ListView

from users_page.forms import UserRegistrationForm, UserEmailLogin, UserPhoneLogin
from .utils import CatalogMixin
    
    
class Catalog(CatalogMixin, ListView):
    
    def get(self, request):
        return self.renderPage(request, 'catalog/catalog.html')


class AboutProduct(CatalogMixin, ListView):
    
    def get(self, request):
        return self.renderPage(request, 'catalog/aboutProduct.html')

         
class ProductComparison(CatalogMixin, ListView):
    
    def get(self, request):
        return self.renderPage(request, 'catalog/productComparison.html')
    