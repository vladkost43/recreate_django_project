from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Comments
from review.models import Review


class CommentsCreateView(LoginRequiredMixin, CreateView):
    model = Comments
    fields = ['text', ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        review = get_object_or_404(Review, pk=self.kwargs['pk'])
        form.instance.review = review
        return super(CommentsCreateView, self).form_valid(form)


class CommentsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comments
    fields = ['text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CommentsUpdateView, self).form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.user == self.request.user:
            return True
        return False


class CommentsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comments
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if post.user == self.request.user:
            return True
        return False
