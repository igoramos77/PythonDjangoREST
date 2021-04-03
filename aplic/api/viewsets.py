from rest_framework import viewsets
from aplic.api import serializers
from aplic import models


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LivroSerializer
    queryset = models.Livro.objects.all()