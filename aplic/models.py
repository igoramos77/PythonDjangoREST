from django.db import models
from uuid import uuid4


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return filename


class CategoriaAtividadeComplementar(models.Model):
    external_id = models.UUIDField(default=uuid4, editable=False)
    macroatividades = models.CharField('Macroatividades', max_length=55)
    carga_horaria_maxima_categoria = models.IntegerField('Carga Horária Máxima da Categoria para este Curso')
    descricao = models.TextField('Descrição', max_length=500, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria Atividade Complementar'
        verbose_name_plural = 'Categorias Atividades Complementares'

    def __str__(self):
        return f"{self.macroatividades}"


class Curso(models.Model):
    external_id = models.UUIDField(default=uuid4, editable=False)
    nome = models.CharField('Nome', max_length=55)
    minimo_categorias = models.IntegerField('Quantidade Mínima de Categorias')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return f"{self.nome} / {self.minimo_categorias} / {self.create_at}"


# Classe associativa
class CategoriaCurso(models.Model):
    external_id = models.UUIDField(default=uuid4, editable=False)
    curso = models.ForeignKey(Curso, null=True, on_delete=models.DO_NOTHING)
    categoria_atividade_complementar = models.ManyToManyField(CategoriaAtividadeComplementar)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria Curso'
        verbose_name_plural = 'Categorias Cursos'

    def __str__(self):
        return f"{self.categoria_atividade_complementar} "


class Usuario(models.Model):
    external_id = models.UUIDField(default=uuid4, editable=False)
    nome = models.CharField('Nome', max_length=55)
    sobrenome = models.CharField('Sobrenome', max_length=255)
    email = models.EmailField('Email', max_length=255)
    senha = models.CharField('Senha', max_length=55)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return f"{self.id} / {self.nome} / {self.sobrenome} / {self.email} / {self.create_at}"


class Aluno(Usuario):
    matricula = models.CharField(unique=True, max_length=55)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return f"{self.matricula} / {self.nome} {self.sobrenome}"


class AtividadeComplementar(models.Model):
    external_id = models.UUIDField(default=uuid4, editable=False)
    aluno = models.ForeignKey(Aluno, null=True, on_delete=models.DO_NOTHING)
    descricao = models.CharField('Descrição', max_length=255)
    empresa = models.CharField('Empresa/Instituição', max_length=55)
    carga_horaria_informada = models.IntegerField('Carga Horária Informada')
    carga_horaria_integralizada = models.IntegerField('Carga Horária Integralizada', null=True, blank=True)
    certificado_img = models.FileField('Certificado', null=True, blank=True, upload_to=get_file_path)
    categoria = models.ForeignKey(CategoriaCurso, null=True, on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Atividade Complementar'
        verbose_name_plural = 'Atividades Complementares'

    def __str__(self):
        return f"{self.descricao} / {self.carga_horaria_informada}"


class Estado(models.Model):
    external_id = models.UUIDField(default=uuid4, editable=False)
    uf = models.CharField('UF', unique=True, max_length=2)
    estado = models.CharField('Estado', max_length=55)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return f"{self.id} / {self.uf} / {self.estado}"


class Instituicao(models.Model):
    external_id = models.UUIDField(default=uuid4, editable=False)
    nome = models.CharField('Nome', max_length=255)

    class Meta:
        verbose_name = 'Instituição'
        verbose_name_plural = 'Instituições'

    def __str__(self):
        return f"{self.id} / {self.nome}"


class Campus(models.Model):
    external_id = models.UUIDField(default=uuid4, editable=False)
    cep = models.CharField('CEP', max_length=9)
    logradouro = models.CharField('Logradouro', max_length=255)
    numero = models.CharField('Numero', max_length=9)
    complemento = models.CharField('Complemento', max_length=255, blank=True)
    bairro = models.CharField('Bairro', max_length=55)
    cidade = models.CharField('Cidade', max_length=55)
    estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING)
    instituicao = models.ForeignKey(Instituicao, related_name='campus', on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = 'Campus'

    def __str__(self):
        return f"{self.instituicao} / {self.logradouro} / {self.numero} / {self.cidade} / {self.estado}"
