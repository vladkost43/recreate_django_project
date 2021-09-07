# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Review
from blog.models import Books


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['text', ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        book = get_object_or_404(Books, pk=self.kwargs['pk'])
        form.instance.book = book
        return super(ReviewCreateView, self).form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ReviewUpdateView, self).form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.user == self.request.user:
            return True
        return False


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if post.user == self.request.user:
            return True
        return False
