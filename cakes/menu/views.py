
from django.shortcuts import render

from menu.models import MenuFlower, FlowerCategory
from blog.models import Posts



# Create your views here.

def index(request):
    flower = MenuFlower.objects.all()
    posts = Posts.objects.all()

    context = {'flower': flower, 'posts': posts}
    return render(request, 'menu/index.html', context)

def catalog(request):
    flowers = MenuFlower.objects.all()

    context = {'flowers': flowers}

    return render(request, 'menu/shop-fullwidth-list.html', context)

def flower_details(request, pk):
    flowers_d = MenuFlower.objects.get(pk=pk)
    # category = FlowerCategory.objects.get()

    context = {'flowers_d': flowers_d}
    return render(request,'menu/product-details.html', context)