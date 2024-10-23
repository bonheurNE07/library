from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    """ ListCreateAPIView requires two mandatory attributes, serializer_class and queryset """

    # We specify BookSerializer which we have early implemented in the serializers module
    queryset = Book.objects.all()
    serilizer_class = BookSerializer
    