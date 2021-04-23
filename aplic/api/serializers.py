from rest_framework import serializers

from aplic import models


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresa
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Curso
        fields = '__all__'


class AlunoSerializer(serializers.ModelSerializer):
    curso = CursoSerializer(read_only=True, many=False)
    #   curso = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='curso-detail')
    #   curso = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Aluno
        fields = '__all__'


class InstituicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instituicao
        fields = '__all__'


class CampusSerializer(serializers.ModelSerializer):
    instituicao = InstituicaoSerializer(read_only=True, many=False)

    class Meta:
        model = models.Campus
        fields = '__all__'


class CategoriaAtividadeComplementarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoriaAtividadeComplementar
        fields = '__all__'


class AtividadeComplementarSerializer(serializers.ModelSerializer):
    categoria = CategoriaAtividadeComplementarSerializer(read_only=True, many=False)
    empresa = EmpresaSerializer(read_only=True, many=False)
    aluno = AlunoSerializer(read_only=True, many=False)

    class Meta:
        model = models.AtividadeComplementar
        fields = '__all__'


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresa
        fields = '__all__'
