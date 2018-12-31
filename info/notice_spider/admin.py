<<<<<<< HEAD
from django.contrib import admin
from .models import Notice


# Register your models here.
@admin.register(Notice)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['seq', 'sort', 'title', 'url', 'tags']
=======
from django.contrib import admin
from .models import Notice


# Register your models here.
@admin.register(Notice)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['seq', 'sort', 'title', 'url', 'tags']
>>>>>>> bfc488ad51715cf21e4e02fbe4765263f013a6aa
