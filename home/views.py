from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .models import Setting, ContactForm, ContactMessage
from django.contrib import messages
from product.models import Category, Product
# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')[:4]
    products_latest = Product.objects.all().order_by('-id')[:4]
    products_picked = Product.objects.all().order_by('?')[:4]
    page = "home"
    context = {'setting': setting, 'page':page, 'category': category, 'products_slider':products_slider,
    'product_latest':products_latest,
    'products_picked':products_picked}
    
    return render(request, 'index.html', context)

def aboutus(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'about.html', context)

def contacts(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            qs = ContactMessage()
            qs.name = form.cleaned_data['name']
            qs.email = form.cleaned_data['email']
            qs.subject = form.cleaned_data['subject']
            qs.message = form.cleaned_data['message']
            qs.ip = request.META.get('REMOTE_ADDR')
            qs.save()
            messages.success(request, "Your message has been sent , we will respond soon !!") 
            return HttpResponseRedirect('/contacts/')
    setting = Setting.objects.get(pk=1)
    form = ContactForm
    context = {'setting': setting, 'form': form}
    
    return render(request, 'contact.html', context)

def category_products(request, id, slug):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    context = {'category': category, 'products':products}
    
    return render(request, 'category_products.html', context)