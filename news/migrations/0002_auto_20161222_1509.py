# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-22 12:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vkwall',
            options={'verbose_name': 'Новость из ВК', 'verbose_name_plural': 'Новости из ВК'},
        ),
    ]
