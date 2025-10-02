
from django.shortcuts import render
from menu.models import MenuCake


# Create your views here.

def index(request):
    cake = MenuCake.objects.all()

    context = {'cake': cake}
    return render(request, 'menu/index.html', context)
