# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Books
from django.db.models import Q


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class PostListView(ListView):
    model = Books
    template_name = 'blog/books_list.html'
    context_object_name = 'posts'
    ordering = ['-book_name']
    paginate_by = 10


class PostDetailView(DetailView):
    model = Books


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Books
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Books
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostUpdateView, self).form_valid(form)

    def test_func(self):
        post = self.get_object()
        auths = post.authors.all()
        for auth in auths:
            if auth.first_name == self.request.user.first_name and auth.last_name == self.request.user.last_name:
                return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Books
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        auths = post.authors.all()
        for auth in auths:
            if auth.first_name == self.request.user.first_name and auth.last_name == self.request.user.last_name:
                return True
        return False


class BooksSearchView(ListView):
    paginate_by = 10
    context_object_name = 'posts'
    ordering = ['-last_name']

    def get_queryset(self):
        q = self.request.GET.get("q")
        return Books.objects.filter(Q(book_name__icontains=q))

    def get_context_data(self, *args, **kwargs):
        context = super(BooksSearchView, self).get_context_data(*args, **kwargs)
        context["q"] = 'q={0}&'.format(self.request.GET.get("q"))
        return context
