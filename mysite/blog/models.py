# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from authors.models import Authors


class Books(models.Model):

    book_name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    authors = models.ManyToManyField(Authors)

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['book_name']
