from django.contrib import admin
from .models import Jokbo


# Register your models here.
@admin.register(Jokbo)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['admit', 'author', 'file', 'department', 'major', 'subject', 'year', 'semester', 'term', 'grade']
