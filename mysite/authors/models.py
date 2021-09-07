# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.urls import reverse


class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    biography = models.TextField(max_length=1000)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return "{0}, {1}".format(self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('auth_id',
                       kwargs={
                           'auth_id': self.pk
                       }
                       )
