from django.contrib import admin
from .models import MenuFlower, FlowerCategory
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

# Register your models here.

# Вопрос с составлением админки

class PostAdminFlower(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = MenuFlower
        fields = '__all__'


class MenuCakeAdmin(admin.ModelAdmin):
    form = PostAdminFlower
    # показывает,какие поля будут видны в админке
    list_display = ('name','price','discount','description')

    # делаем выбранные графы кликабельными в админке
    list_display_links = ('name','price')

    # добавили поиск по полям
    search_fields = ('name','price')

    # добавили фильтр по полям
    list_filter = ('name','price','description')


admin.site.register(MenuFlower, MenuCakeAdmin)
admin.site.register(FlowerCategory)
