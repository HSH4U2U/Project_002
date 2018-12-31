<<<<<<< HEAD
from django.contrib import admin
from .models import Profile


# Register your models here.
@admin.register(Profile)
class CategoryAdmin(admin.ModelAdmin):
=======
from django.contrib import admin
from .models import Profile


# Register your models here.
@admin.register(Profile)
class CategoryAdmin(admin.ModelAdmin):
>>>>>>> bfc488ad51715cf21e4e02fbe4765263f013a6aa
    list_display = ['user', 'email', 'telegram_id', 'my_tags', 'my_jokbo']