# Generated by Django 2.2.19 on 2021-04-10 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0004_auto_20210410_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividadecomplementar',
            name='categoria',
        ),
    ]