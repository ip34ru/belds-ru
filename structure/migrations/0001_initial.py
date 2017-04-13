# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-22 19:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menu_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Документ')),
                ('name', models.CharField(max_length=1024)),
            ],
            options={
                'verbose_name_plural': 'Элементы меню',
                'verbose_name': 'Элемент меню',
            },
        ),
        migrations.CreateModel(
            name='menu_main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Названия пунктов',
                'verbose_name': 'Название пункта',
            },
        ),
        migrations.AddField(
            model_name='menu_item',
            name='caption',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.menu_main'),
        ),
    ]
