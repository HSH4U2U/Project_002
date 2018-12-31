<<<<<<< HEAD
from django.db import models


# Create your models here.
class Notice(models.Model):
    seq = models.IntegerField(verbose_name='번호',)
    sort = models.TextField(verbose_name='카테고리',)
    title = models.TextField(verbose_name='제목',)
    url = models.TextField(verbose_name='링크',)
    tags = models.TextField(verbose_name='태그 리스트',)
=======
from django.db import models


# Create your models here.
class Notice(models.Model):
    seq = models.IntegerField(verbose_name='번호',)
    sort = models.TextField(verbose_name='카테고리',)
    title = models.TextField(verbose_name='제목',)
    url = models.TextField(verbose_name='링크',)
    tags = models.TextField(verbose_name='태그 리스트',)
>>>>>>> bfc488ad51715cf21e4e02fbe4765263f013a6aa
