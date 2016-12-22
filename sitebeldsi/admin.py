from django.contrib import admin
from django.conf import settings
from django.core.files.storage import DefaultStorage
from filebrowser.sites import FileBrowserSite


filebrowser_site = FileBrowserSite(name='filebrowser', storage=DefaultStorage())
filebrowser_site.directory = "documents/"

admin.autodiscover()
admin.site.site_title =  settings.ADMIN_SITE_TITLE or 'My site admin'
admin.site.site_header = settings.ADMIN_SITE_HEADER or 'My administration'
admin.site.index_title = settings.ADMIN_INDEX_TITLE or 'Site administration'

