from django.conf.urls import url
from .views import AuthorsView, BooksView, AuthorsDetailView, BooksDetailView
app_name = "authors"

urlpatterns = [
    url(r'^authors/$', AuthorsView.as_view()),
    url(r'^books/$', BooksView.as_view()),
    url(r'^authors/(?P<pk>\d+)/$', AuthorsDetailView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', BooksDetailView.as_view()),
]
