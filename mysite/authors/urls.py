from . import views

from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', AuthorListView.as_view(), name='author-home'),
    url(r'^post/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^search/$', AuthorSearchView.as_view(), name='author-search')
]
