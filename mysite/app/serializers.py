from rest_framework import serializers
from blog.models import Books
from authors.models import Authors


class AuthorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Authors
        fields = ['pk', 'first_name', 'last_name', 'biography']


class BooksSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Books
        fields = ['pk', 'book_name', 'description', 'authors']

