# Generated by Django 2.1 on 2018-12-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asitis', '0002_auto_20181220_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='course',
            field=models.CharField(default='1', max_length=8, verbose_name='교양/전공 여부'),
            preserve_default=False,
        ),
    ]
