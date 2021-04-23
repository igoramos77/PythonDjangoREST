# Generated by Django 2.2.19 on 2021-04-11 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0008_auto_20210410_2050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluno',
            options={'ordering': ['id'], 'verbose_name': 'Aluno', 'verbose_name_plural': 'Alunos'},
        ),
        migrations.AlterModelOptions(
            name='atividadecomplementar',
            options={'ordering': ['id'], 'verbose_name': 'Atividade Complementar', 'verbose_name_plural': 'Atividades Complementares'},
        ),
        migrations.AlterModelOptions(
            name='campus',
            options={'ordering': ['id'], 'verbose_name': 'Campus', 'verbose_name_plural': 'Campus'},
        ),
        migrations.AlterModelOptions(
            name='categoriaatividadecomplementar',
            options={'ordering': ['id'], 'verbose_name': 'Categoria Atividade Complementar', 'verbose_name_plural': 'Categorias Atividades Complementares'},
        ),
        migrations.AlterModelOptions(
            name='categoriacurso',
            options={'ordering': ['id'], 'verbose_name': 'Categoria Curso', 'verbose_name_plural': 'Categorias Cursos'},
        ),
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ['id'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterModelOptions(
            name='empresa',
            options={'ordering': ['razao_social'], 'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
        migrations.AlterModelOptions(
            name='estado',
            options={'ordering': ['id'], 'verbose_name': 'Estado', 'verbose_name_plural': 'Estados'},
        ),
        migrations.AlterModelOptions(
            name='instituicao',
            options={'ordering': ['id'], 'verbose_name': 'Instituição', 'verbose_name_plural': 'Instituições'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['id'], 'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
    ]