# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-05 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20160504_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='post',
            name='logo',
            field=models.ImageField(default='logo/default/pizza.png', upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='siteusername',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bgImg',
            field=models.ImageField(default='bg/default.jpg', upload_to='bg/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='profileImg',
            field=models.ImageField(default='pic/default.jpg', upload_to='pic/'),
        ),
    ]
