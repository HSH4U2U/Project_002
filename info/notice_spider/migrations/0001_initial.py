# Generated by Django 2.1 on 2018-12-15 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq', models.IntegerField(verbose_name='번호')),
                ('sort', models.TextField(verbose_name='카테고리')),
                ('title', models.TextField(verbose_name='제목')),
                ('url', models.TextField(verbose_name='링크')),
                ('tags', models.TextField(blank=True, verbose_name='태그 리스트')),
            ],
        ),
    ]
