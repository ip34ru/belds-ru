# coding=utf-8
from afisha.views import afishaView
from arhiv.views import arhivView
from blankform.views import blankForm, comment
from docs.views import docsView
from filebrowser.sites import site
from django.conf.urls import patterns, include, url
from django.contrib import admin
from info.views import infoView
from news.views import newsView
from professors.views import professorsView
from flat_pages.views import  FlatPageIndex, FlatPageView

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static


admin.autodiscover()
admin.site.site_title =  settings.ADMIN_SITE_TITLE or 'My site admin'
admin.site.site_header = settings.ADMIN_SITE_HEADER or 'My administration'
admin.site.index_title = settings.ADMIN_INDEX_TITLE or 'Site administration'

urlpatterns = (
    url(r'^$', FlatPageIndex.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/', include(site.urls)),
)
urlpatterns += ( 
# Свои приложения: ------------------------------------------
    # Professors ------
    url(r'^professors/', professorsView),
    # -----------------
    # docs ------------
    url(r'^docs/', docsView),
    # -----------------
    # info ------------
    url(r'^info/', infoView),
    # -----------------
    # news ------------
    url(r'^news/', newsView),
    # -----------------
    # afisha ----------
    url(r'^afisha/', afishaView),
    # -----------------
    # arhiv -----------
    url(r'^arhiv/', arhivView),
    # -----------------
    # Ссылка на страницу опроса:
    url(r'blankform/', blankForm),
    url(r'commentform/', comment),
    #-----------------------------
# -----------------------------------------------------------

# Свои приложения: ------------------------------------------
    # Django Basic File Manager ------
#    url(r'^files/', include('django_bfm.urls')),
#    url(r'^media', ),
    # -----------------
# -----------------------------------------------------------
url(r'^(?P<url>.*/)$', FlatPageView.as_view()),
) 
#urlpatterns += (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT ),)

