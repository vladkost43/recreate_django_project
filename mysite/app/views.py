# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.response import Response
from rest_framework.views import APIView
from authors.models import Authors
from blog.models import Books
from .serializers import AuthorsSerializer, BooksSerializer
from rest_framework.generics import RetrieveAPIView

class AuthorsView(APIView):

    def get(self, request):
        authors = Authors.objects.all()
        serializer = AuthorsSerializer(authors, many=True)
        return Response({"authors": serializer.data})


class BooksView(APIView):

    def get(self, request):
        authors = Books.objects.all()
        serializer = BooksSerializer(authors, many=True)
        return Response({"books": serializer.data})


class AuthorsDetailView(RetrieveAPIView):

    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer


class BooksDetailView(RetrieveAPIView):

    queryset = Books.objects.all()
    serializer_class = BooksSerializer
