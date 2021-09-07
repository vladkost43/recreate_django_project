# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from blog.models import Books
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
User = get_user_model()


class Review(models.Model):

    text = models.TextField(max_length=5000)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        verbose_name="Author od comment",
        on_delete=models.CASCADE
    )

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.book.pk})

    class Meta:
        ordering = ['book']

    def __str__(self):
        return '{0} {1} {2}'.format(self.user.first_name, self.user.last_name, self.book.book_name)
