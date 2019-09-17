from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^article-list/(?P<article_column>[-\w]+)/$',views.article_list,name = "article_list"),
    url(r'^blog/$',views.blog,name = "blog"),
    url(r'^article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$' ,views.article_detail,name = "article_detail"),
]
