from rest_framework import serializers
from .models import Book, BookNumber, Character, Auhtor


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name']


class AuhtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auhtor
        fields = ['id', 'name', 'surname']


class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    characters = CharacterSerializer(many=True)
    auhtors = AuhtorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'description',
                  'price', 'is_published', 'published', 'number', 'characters', 'auhtors']
