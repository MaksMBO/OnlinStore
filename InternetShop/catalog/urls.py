from django.urls import path
from . import views

urlpatterns = [
 path('', views.Catalog.as_view(), name="catalog"),
 path('name/', views.AboutProduct.as_view(), name='aboutProduct'),
 path('comparison/', views.ProductComparison.as_view(), name='productComparison'),
]