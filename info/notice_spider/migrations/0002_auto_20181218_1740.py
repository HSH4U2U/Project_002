# Generated by Django 2.1 on 2018-12-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice_spider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='tags',
            field=models.TextField(verbose_name='태그 리스트'),
        ),
    ]
