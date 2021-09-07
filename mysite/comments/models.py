# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from review.models import Review
from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Comments(models.Model):

    user = models.ForeignKey(
        User,
        verbose_name="Author od comment",
        on_delete=models.CASCADE
    )
    text = models.TextField(max_length=1000)
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.review.book.pk})

    class Meta:
        ordering = ['text']

    def __str__(self):
        return '{0} {1} '.format(self.user.first_name, self.user.last_name)
