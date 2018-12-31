<<<<<<< HEAD
from django.db import models
from django.conf import settings


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=16, verbose_name='과목명',)
    professor = models.CharField(max_length=16, verbose_name='교수명', null=True, blank=True)
    code = models.CharField(max_length=8, verbose_name='과목코드',)
    department = models.CharField(max_length=16, verbose_name='소속 대학명',)
    major = models.CharField(max_length=16, verbose_name='전공',)
    course = models.CharField(max_length=8, verbose_name='교양/전공 여부',)
    grade = models.CharField(max_length=8, verbose_name='수강 학년',)
    semester = models.TextField(verbose_name='학기',)


class Jokbo(models.Model):
    STATUS_CHOICES1 = (
        ('파일 검토 중', '파일 검토 중'),
        ('허가', '허가'),
    )
    admit = models.TextField(choices=STATUS_CHOICES1, verbose_name='허가 여부', null=True, blank=True,)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자', null=True,)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='족보 파일',)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='해당 수업')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
=======
from django.db import models
from django.conf import settings


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=16, verbose_name='과목명',)
    professor = models.CharField(max_length=16, verbose_name='교수명', null=True, blank=True)
    code = models.CharField(max_length=8, verbose_name='과목코드',)
    department = models.CharField(max_length=16, verbose_name='소속 대학명',)
    major = models.CharField(max_length=16, verbose_name='전공',)
    course = models.CharField(max_length=8, verbose_name='교양/전공 여부',)
    grade = models.CharField(max_length=8, verbose_name='수강 학년',)
    semester = models.TextField(verbose_name='학기',)


class Jokbo(models.Model):
    STATUS_CHOICES1 = (
        ('파일 검토 중', '파일 검토 중'),
        ('허가', '허가'),
    )
    admit = models.TextField(choices=STATUS_CHOICES1, verbose_name='허가 여부', null=True, blank=True,)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자', null=True,)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='족보 파일',)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='해당 수업')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
>>>>>>> bfc488ad51715cf21e4e02fbe4765263f013a6aa
