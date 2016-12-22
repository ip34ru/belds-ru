# coding=utf-8
__author__ = 'taksenov'

from django.db import models
from django.core.urlresolvers import reverse_lazy
from sitebeldsi.models_mixins import DocumentMixin
# Таблица с преподавателями (основными)
class professors(models.Model):
    fio = models.CharField(max_length=150)
    standing = models.CharField(max_length=150)
    seniority = models.CharField(max_length=150)
    categoty =  models.CharField(max_length=150)
    dateofcategory = models.DateField(null=True)
    education = models.CharField(max_length=150)
    colledge =  models.CharField(max_length=2500)
    isdualjobholder = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return self.fio

# Таблица с преподавателями (дополнительными)
class professors2(models.Model):
    fio = models.CharField(max_length=150)
    standing = models.CharField(max_length=150)
    education = models.CharField(max_length=150)
    categoty =  models.CharField(max_length=150)
    dateofcategory = models.DateField(null=True)

    def __unicode__(self):
        return self.fio

# Таблица с внешними совместителями
class dual_job_holder(models.Model):
    fio = models.CharField(max_length=150)

    def __unicode__(self):
        return self.fio

# таблица с названиями пунктов меню
class menu_main(models.Model):
    caption = models.CharField(max_length=100)

    def __unicode__(self):
        return self.caption

# таблица с элементами из пунктов меню
class menu_item(DocumentMixin, models.Model):
    caption = models.ForeignKey('menu_main')
    name = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name





















