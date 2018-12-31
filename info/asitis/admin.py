<<<<<<< HEAD
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
=======
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
>>>>>>> bfc488ad51715cf21e4e02fbe4765263f013a6aa
