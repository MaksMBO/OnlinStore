from django.shortcuts import render
from django.views.generic.list import ListView

from .utils import CatalogMixin
from .models import Products, ProductsBrand

    
class Catalog(CatalogMixin, ListView):
    
    def get(self, request):
        context = self.renderPage()
        context['products'] = Products.objects.all()
        context['brands'] = ProductsBrand.objects.all()
        return render(request, 'catalog/catalog.html', context=context)


class AboutProduct(CatalogMixin, ListView):
    
    def get(self, request):
        context = self.renderPage()
        return render(request, 'catalog/aboutProduct.html', context=context)

         
class ProductComparison(CatalogMixin, ListView):
    
    def get(self, request):
        context = self.renderPage()
        return render(request, 'catalog/productComparison.html', context=context)
