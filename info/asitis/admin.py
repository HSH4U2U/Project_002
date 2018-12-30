from django.contrib import admin
from .models import Subject, Jokbo


# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'professor', 'code', 'department', 'major', 'course', 'grade', 'semester']


@admin.register(Jokbo)
class JokboAdmin(admin.ModelAdmin):
    # list_display = ['id', 'admit', 'author', 'file', 'subject', 'created_at', 'updated_at']
    list_display = ['id', 'admit', 'author', 'file', 'created_at', 'updated_at']
