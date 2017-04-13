# coding=utf-8
from afisha.views import afishaView
from arhiv.views import arhivView
from blankform.views import blankForm, comment
from docs.views import docsView


from django.conf.urls import patterns, include, url

from info.views import InfoDocumentsList
from structure.views import StructureDocumentsList
from gto.views import GtoDocumentsList
from news.views import newsView
from professors.views import professorsView
from flat_pages.views import  FlatPageIndex, FlatPageView

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from .admin import filebrowser_site, admin





urlpatterns = (
    url(r'^$', FlatPageIndex.as_view()),
    url(r'^admin/filebrowser/', include(filebrowser_site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
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
    url(r'^info/', InfoDocumentsList.as_view()),
    url(r'^structure/', StructureDocumentsList.as_view()),
    url(r'^gto/', GtoDocumentsList.as_view()),
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
    url(r'^(?P<url>.*/)$', FlatPageView.as_view()),
)
