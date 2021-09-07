# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)
from authors.models import Authors
from django import forms


class SearchForm(forms.Form):
    q = forms.CharField()


class AuthorListView(ListView):
    model = Authors
    template_name = 'authors/authors_list.html'
    context_object_name = 'posts'
    ordering = ['-last_name']
    paginate_by = 10


class AuthorDetailView(DetailView):
    model = Authors


class AuthorSearchView(ListView):
    paginate_by = 10
    context_object_name = 'posts'
    ordering = ['-last_name']

    def get_queryset(self):
        q = self.request.GET.get("q")
        return Authors.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorSearchView, self).get_context_data(*args, **kwargs)
        context["q"] = 'q={0}&'.format(self.request.GET.get("q"))
        return context


def author_search(request):
    return render(request, 'authors/author_search.html', {'title': 'Author Search'})
