from django.core.paginator import Page, Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from unicodedata import category

from menu.models import MenuFlower, FlowerCategory, OrderFlower
from blog.models import Posts
from django.contrib import messages



# Create your views here.

def index(request):
    flower = MenuFlower.objects.all().order_by('-id')[:7]
    posts = Posts.objects.all().order_by('-created')[:3]

    context = {'flower': flower, 'posts': posts}
    return render(request, 'menu/index.html', context)

def catalog(request):
    flowers = MenuFlower.objects.all()
    category = FlowerCategory.objects.all()

    page = request.GET.get('page')
    results = 3
    paginator = Paginator(flowers, results)

    try:
        flowers = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        flowers = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        flowers = paginator.page(page)

    left_index = int(page) - 3

    if left_index < 1:
        left_index = 1

    right_index = int(page) + 4

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    context = {'flowers': flowers, 'category': category, 'custom_range': custom_range, 'paginator': paginator}

    return render(request, 'menu/shop-fullwidth-list.html', context)

def flower_details(request, pk):
    flowers_d = MenuFlower.objects.get(pk=pk)
    # category = FlowerCategory.objects.get()

    context = {'flowers_d': flowers_d}
    return render(request,'menu/product-details.html', context)

def order_flower(request):
    if request.method == "POST":
        flower_id = request.POST.get('flower_id')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        # проверяю на пустые поля
        if name and surname and email and phone_number:
            OrderFlower.objects.create(
                flower_id=flower_id,
                name=name,
                surname=surname,
                email=email,
                phone_number=phone_number,
                message=message,
            )
            messages.success(request, 'Заказ успешно принят! Мы свяжемся с вами.')
        else:
            messages.error(request, 'Пожалуйста, заполните все обязательные поля.')

    return redirect('menu.catalog')