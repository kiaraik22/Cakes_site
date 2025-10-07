from django.contrib import admin
from .models import MenuCake, FlowerCategory

# Register your models here.

# Вопрос с составлением админки

class MenuCakeAdmin(admin.ModelAdmin):
    # показывает,какие поля будут видны в админке
    list_display = ('name','price','discount','description')

    # делаем выбранные графы кликабельными в админке
    list_display_links = ('name','price')

    # добавили поиск по полям
    search_fields = ('name','price')

    # добавили фильтр по полям
    list_filter = ('name','price','description')


admin.site.register(MenuCake, MenuCakeAdmin)
admin.site.register(FlowerCategory)
