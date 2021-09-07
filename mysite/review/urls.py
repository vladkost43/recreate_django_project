
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^review/(?P<pk>\d+)/add/$', ReviewCreateView.as_view(), name='review-create'),
    url(r'^review/(?P<pk>\d+)/update/$', ReviewUpdateView.as_view(), name='review-update'),
    url(r'^review/(?P<pk>\d+)/delete/$', ReviewDeleteView.as_view(), name='review-delete'),
]
