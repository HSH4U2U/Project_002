<<<<<<< HEAD
# Generated by Django 2.1 on 2018-12-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='tags',
        ),
        migrations.AddField(
            model_name='profile',
            name='my_jokbo',
            field=models.TextField(blank=True, verbose_name='내가 선택한 족보'),
        ),
        migrations.AddField(
            model_name='profile',
            name='my_tags',
            field=models.TextField(blank=True, verbose_name='내가 선택한 태그'),
        ),
    ]
=======
# Generated by Django 2.1 on 2018-12-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='tags',
        ),
        migrations.AddField(
            model_name='profile',
            name='my_jokbo',
            field=models.TextField(blank=True, verbose_name='내가 선택한 족보'),
        ),
        migrations.AddField(
            model_name='profile',
            name='my_tags',
            field=models.TextField(blank=True, verbose_name='내가 선택한 태그'),
        ),
    ]
>>>>>>> bfc488ad51715cf21e4e02fbe4765263f013a6aa
