from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .utils import CatalogMixin
from .models import Products, ProductsBrand

    
class Catalog(CatalogMixin, ListView):
    
    def get(self, request):
        context = self.renderPage()
        context['products'] = Products.objects.all().prefetch_related('img').only(
            'title', 'price', 'img', 'type', 'brand', 'is_available',
        )
        context['brands'] = ProductsBrand.objects.all()
        return render(request, 'catalog/catalog.html', context=context)


class AboutProduct(CatalogMixin, DetailView):
    
    pk_url_kwarg = 'id'
    
    def get(self, request, *args, **kwargs):
        context = self.renderPage()
        context['product'] = Products.objects.filter(id=self.kwargs.get("id")).prefetch_related('img').only(
            'title', 'price', 'img', 'type', 'brand', 'is_available',
        ).first()
        return render(request, 'catalog/aboutProduct.html', context=context)

         
class ProductComparison(CatalogMixin, ListView):
    
    def get(self, request):
        context = self.renderPage()
        return render(request, 'catalog/productComparison.html', context=context)
