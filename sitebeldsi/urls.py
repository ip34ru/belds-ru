# coding=utf-8
from afisha.views import afishaView
from arhiv.views import arhivView
from blankform.views import blankForm, comment
from docs.views import docsView
from django.contrib.flatpages import views
from filebrowser.sites import site
from django.conf.urls import patterns, include, url
from django.contrib import admin
from info.views import infoView
from news.views import newsView
from professors.views import professorsView

from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = (
    url(r'^$', 'django.contrib.flatpages.views.flatpage', {'url': '/index/'}, name='index'),
#    url(r'^pages/$', include('django.contrib.flatpages.urls')),
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
url(r'^(?P<url>.*/)$', views.flatpage),
) 
#urlpatterns += (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT ),)

