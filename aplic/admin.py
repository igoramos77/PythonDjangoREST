from django.contrib import admin

from .models import Livro, Usuario, Aluno, Estado, Instituicao, Campus, Curso, CategoriaAtividadeComplementar, CategoriaCurso, AtividadeComplementar


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'create_at')


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'create_at')


@admin.register(Aluno)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'matricula', 'nome', 'sobrenome', 'email', 'create_at')


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'uf')


@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('id', 'instituicao', 'logradouro', 'numero', 'estado', 'create_at')


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'minimo_categorias', 'create_at')


@admin.register(CategoriaAtividadeComplementar)
class CategoriaAtividadeComplementarAdmin(admin.ModelAdmin):
    list_display = ('id', 'macroatividades', 'create_at')


@admin.register(CategoriaCurso)
class CategoriaCursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'curso', 'create_at')


@admin.register(AtividadeComplementar)
class AtividadeComplementarAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'carga_horaria_informada', 'carga_horaria_integralizada', 'create_at')
