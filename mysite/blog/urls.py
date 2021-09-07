from . import views
from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^about/$', about, name='about'),
    url(r'^$', PostListView.as_view(), name='blog-home'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^post/new/$', PostCreateView.as_view(), name='post-create'),
    url(r'^post/(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='post-update'),
    url(r'^post/(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='post-delete'),
    url(r'^search_book/$', BooksSearchView.as_view(), name='books-search')
]
