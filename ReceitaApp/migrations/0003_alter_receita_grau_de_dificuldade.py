# Generated by Django 4.2.7 on 2023-11-08 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReceitaApp', '0002_alter_receita_grau_de_dificuldade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='grau_de_dificuldade',
            field=models.CharField(choices=[('F', 'Facil'), ('M', 'Moderado'), ('D', 'Dificil')], max_length=10),
        ),
    ]
