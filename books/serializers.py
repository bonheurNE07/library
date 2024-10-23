from datetime import date

from rest_framework import serializers
from .models import Book

# BookSerializer definition
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book

        fields = ['id','title','author_name', 'published_date', 'language']
        read_only_fields = ['id','published_date']
    
    # exemple of field-level validation
    def validate_title(self, value):
        if value == "":
            raise serializers.ValidationError("Title cannot be Empty.")
        elif value == "Untitled":
            raise serializers.ValidationError("Title cannot be 'Untitled'.")
        return value
    
    # example of object-level validation
    def validate(self, data):
        """
        This is used only to validate the entire object (multiple fields together)
        """
        if data['published_date'] > date.today():
            raise serializers.ValidationError("Published date cannot be in the future")
        if data['author_name'].isdigit():
            raise serializers.ValidationError("Authors name cannot be digits.")
        if data['language'].isdigit():
            raise serializers.ValidationError("Books language cannot be digits.")
        
        return data