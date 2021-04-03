from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Livro

@api_view()
def livros_view(request):
    livros = Livro.objects.all()
    output = [{
        'nome': livro.nome,
        'autor': livro.autor,
        'categoria': livro.categoria
    } for livro in livros]

    return Response(output)
