# Generated by Django 2.2.19 on 2021-04-05 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0003_atividadecomplementar_aluno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Curso'),
        ),
    ]