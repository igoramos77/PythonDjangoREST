from django.db import models
from uuid import uuid4


class Livro(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField('Título', max_length=255)
    author = models.CharField('Autor', max_length=255)
    release_year = models.IntegerField('Ano')
    state = models.CharField('Estado', max_length=50)
    pages = models.IntegerField('Páginas')
    publishing_company = models.CharField('Editora', max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

