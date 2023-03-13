from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.db.models import Q

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

class FilterProducts(CatalogMixin, ListView):
    
    def get(self, request):
        query = Products.objects.filter(
            Q(brand__brand__in=self.request.GET.getlist('brand')) &
            Q(price__gte=self.request.GET.get('price_start'), price__lte=self.request.GET.get('price_end'))
            ) 
        context = self.renderPage()
        context['products'] = Products.objects.all().prefetch_related('img').only(
            'title', 'price', 'img', 'type', 'brand', 'is_available',
        )
        context['brands'] = ProductsBrand.objects.all()
        context['query'] = query
        return render(request, 'catalog/catalog.html', context=context)
    
class FilterProductsJson(CatalogMixin, ListView):
    def get_queryset(self):
        all_brands = [i.brand for i in ProductsBrand.objects.all()]
        if not self.request.GET.get("brand", False):
            brand =  Q(brand__brand__in=all_brands)
        else:
            brand = Q(brand__brand__in=self.request.GET.getlist('brand'))
       
        query = Products.objects.filter(
            brand &
            Q(price__gte=self.request.GET.get('price_start'), price__lte=self.request.GET.get('price_end'))
            ).prefetch_related('img').values('title', 'price', 'img__img', 'id').distinct()
    
        return query

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())  
        temp = []
        temp.clear()

        my_len = len(queryset)    
        i = 0
        while i < my_len:
            if queryset[i]['title'] not in temp:
                temp.append(queryset[i]['title'])
                # queryset[i]['url'] = 
                i += 1
            else:
                del queryset[i]
                my_len -= 1

        return JsonResponse({"movies": queryset}, safe=False)
    