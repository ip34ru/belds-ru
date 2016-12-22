
from django.db import models
from filebrowser.fields import FileBrowseField

class DocumentMixin(models.Model):
    document = FileBrowseField("Документ", max_length=200, directory="documents/", blank=True, null=True)

    class Meta:
        abstract = True

    @property
    def link(self):
        return document.url