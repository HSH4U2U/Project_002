from django.db import models
from django.conf import settings


# Create your models here.
class Jokbo(models.Model):
    STATUS_CHOICES1 = (
        ('파일 검토 중', '파일 검토 중'),
        ('허가', '허가'),
    )
    admit = models.TextField(choices=STATUS_CHOICES1, verbose_name='다시 먹을 지 여부', null=True, blank=True,)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자', null=True,)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='족보 파일',)
    department = models.TextField(blank=True, verbose_name='00대학',)
    major = models.TextField(blank=True, verbose_name='전공',)
    subject = models.TextField(blank=True, verbose_name='강의명',)
    STATUS_CHOICES2 = (
        (2010, '2010'),
        (2011, '2011'),
        (2012, '2012'),
        (2013, '2013'),
        (2014, '2014'),
        (2015, '2015'),
        (2016, '2016'),
        (2017, '2017'),
        (2018, '2018'),
        (2019, '2019'),
    )
    year = models.IntegerField(choices=STATUS_CHOICES2, verbose_name='년도', null=True, blank=True,)
    STATUS_CHOICES3 = (
        (1, '1'),
        (2, '2'),
    )
    semester = models.IntegerField(choices=STATUS_CHOICES3, verbose_name='학기', null=True, blank=True,)
    STATUS_CHOICES4 = (
        ('중간', '중간'),
        ('기말', '기말'),
        ('기타', '기타'),
    )
    term = models.CharField(max_length=2, choices=STATUS_CHOICES4, verbose_name='중간/기말/기타', null=True, blank=True,)
    STATUS_CHOICES5 = (
        (1, '1'),
        (2.5, '2~3'),
        (4, '4'),
    )
    grade = models.IntegerField(choices=STATUS_CHOICES5, verbose_name='학년', null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
