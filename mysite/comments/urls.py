from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^add/(?P<pk>\d+)/$', CommentsCreateView.as_view(), name='comments-create'),
    url(r'^update/(?P<pk>\d+)/$', CommentsUpdateView.as_view(), name='comments-update'),
    url(r'^delete/(?P<pk>\d+)/$', CommentsDeleteView.as_view(), name='comments-delete'),
]
