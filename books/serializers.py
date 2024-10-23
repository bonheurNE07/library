from rest_framework import serializers
from .models import Book

# BookSerializer definition
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book

        fields = ['id','title','author_name', 'published_date', 'language']
        read_only_fields = ['id','published_date']
        
    def validate_title(self, value):
        if value == "":
            raise serializers.ValidationError("Title cannot be Empty.")
        elif value == "Untitled":
            raise serializers.ValidationError("Title cannot be 'Untitled'.")
        return value