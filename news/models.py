__author__ = 'taksenov'
#coding: utf-8

from django.db import models

class vkwall(models.Model):
    news_text = models.CharField(max_length=5000)
    datetime = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Новость из ВК'
        verbose_name_plural = 'Новости из ВК'

    def __str__(self):
        return self.news_text[:100]

