# Generated by Django 2.2.19 on 2021-04-10 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0007_auto_20210410_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividadecomplementar',
            name='aluno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='aluno', to='aplic.Aluno'),
        ),
    ]