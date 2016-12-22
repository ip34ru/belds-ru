# coding=utf-8
__author__ = 'taksenov'

from django.db import models

# таблица с названиями пунктов меню
class menu_main(models.Model):
    caption = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Название пункта'
        verbose_name_plural = 'Названия пунктов'


    def __str__(self):
        return self.caption


# таблица с элементами из пунктов меню
class menu_item(models.Model):
    caption = models.ForeignKey('menu_main')
    name = models.CharField(max_length=1024)
    link = models.CharField(max_length=1024)

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'


    def __str__(self):
        return self.name




















