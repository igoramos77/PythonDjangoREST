from django.urls import path, include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers


from aplic.api import viewsets as usuario
from aplic.api import viewsets as aluno
from aplic.api import viewsets as instituicao
from aplic.api import viewsets as campus
from aplic.api import viewsets as curso
from aplic.api import viewsets as categoriaatividadecomplementar
from aplic.api import viewsets as atividadecomplementar


route = routers.DefaultRouter()

route.register(r'usuarios', usuario.UsuarioViewSet, basename="Usuarios")
route.register(r'alunos', aluno.AlunoViewSet, basename="Alunos")
route.register(r'instituicoes', instituicao.InstituicaoViewSet, basename="Instituicoes")
route.register(r'campus', campus.CampusViewSet, basename="Campus")
route.register(r'cursos', curso.CursoViewSet, basename="Curso")
route.register(r'categorias-atividades-complementares', categoriaatividadecomplementar.CategoriaAtividadeComplementarViewSet, basename="CategoriaAtividadesComplementares")
route.register(r'atividades-complementares', curso.AtividadeComplementarViewSet, basename="AtividadeComplementar")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(route.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
