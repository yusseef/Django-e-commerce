from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),    
    path('contacts/', views.contacts, name='contacts'),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('search/',views.search, name='search'),
    path('search_auto/',views.search_auto, name='search_auto')
]
