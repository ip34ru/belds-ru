from django.db import models


class FlatPage(models.Model):
    url = models.CharField(max_length=15, verbose_name='Ссылка', help_text='Используйте "index" для главной страницы')
    content = models.TextField(verbose_name='Содержимое страницы в формате HTML', help_text='HTML')

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.url

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.url != 'index' and self.url[-1] != '/':
            self.url += '/'
        super(FlatPage, self).save(force_insert=False, force_update=False, using=None,
                                   update_fields=None)
