from django.conf.urls import url
from . import views
from .views import IndexPage, ProjectList, ProjectDetail, ArticleList, ArticleDetail
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    url(r'^$', IndexPage.as_view(), name='index_page'),
    url(r'^projects/$', ProjectList.as_view(), name='project_list'),
    url(r'^projects/(?P<slug>[^/]*)$', ProjectDetail.as_view(), name='project_detail'),
    url(r'^articles/$', ArticleList.as_view(), name='article_list'),
    url(r'^articles/(?P<slug>[^/]*)$', ArticleDetail.as_view(), name='article_detail'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
        url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }),
    ]