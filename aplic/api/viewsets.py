from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from aplic.api import serializers
from aplic import models


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer


class AlunoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    #   mixins.UpdateModelMixin,
    #   mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = models.Aluno.objects.all()
    serializer_class = serializers.AlunoSerializer

    @action(methods=['get'], detail=True)
    def atividades_complementares(self, request, pk=None):
        atividades_complementares = self.get_queryset().order_by('id').last()
        serializer = self.get_serializer_class()(atividades_complementares)
        return Response(serializer.data)


class InstituicaoViewSet(viewsets.ModelViewSet):
    queryset = models.Instituicao.objects.all()
    serializer_class = serializers.InstituicaoSerializer


class CampusViewSet(viewsets.ModelViewSet):
    queryset = models.Campus.objects.all()
    serializer_class = serializers.CampusSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = models.Curso.objects.all()
    serializer_class = serializers.CursoSerializer


class CategoriaAtividadeComplementarViewSet(viewsets.ModelViewSet):
    queryset = models.CategoriaAtividadeComplementar.objects.all()
    serializer_class = serializers.CategoriaAtividadeComplementarSerializer


class AtividadeComplementarViewSet(viewsets.ModelViewSet):
    queryset = models.AtividadeComplementar.objects.all()
    serializer_class = serializers.AtividadeComplementarSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = models.Empresa.objects.all()
    serializer_class = serializers.EmpresaSerializer



