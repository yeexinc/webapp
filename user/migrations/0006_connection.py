# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-04 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_delete_connection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromuser', models.PositiveIntegerField()),
                ('touser', models.PositiveIntegerField()),
            ],
        ),
    ]
