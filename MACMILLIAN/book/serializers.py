from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields = ['title', 'content', 'image', 'content', 'slug', 'author', 'date_published']
        fields = '__all__'