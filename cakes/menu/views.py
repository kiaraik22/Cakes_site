
from django.shortcuts import render
from menu.models import MenuCake
from blog.models import Posts



# Create your views here.

def index(request):
    cake = MenuCake.objects.all()
    posts = Posts.objects.all()

    context = {'cake': cake, 'posts': posts}
    return render(request, 'menu/index.html', context)

def catalog(request):
    flowers = MenuCake.objects.all()

    context = {'flowers': flowers}

    return render(request, 'menu/shop-fullwidth-list.html', context)

def flower_details(request, pk):
    flowers_d = MenuCake.objects.get(pk=pk)
    context = {'flowers_d': flowers_d}
    return render(request,'menu/product-details.html', context)