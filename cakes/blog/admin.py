from django.contrib import admin
from .models import Posts

# Register your models here.

from django.contrib import admin
from .models import Posts

# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    # показывает,какие поля будут видны в админке
    list_display = ('title', 'short_content', 'created')

# Как можно сократить описание в админке?

    # делаем выбранные графы кликабельными в админке
    list_display_links = ('title', 'created')

    # добавили поиск по полям
    search_fields = ('title', 'created')

    # добавили фильтр по полям
    list_filter = ('title', 'created')

admin.site.register(Posts, PostsAdmin)