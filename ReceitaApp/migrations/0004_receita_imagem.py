# Generated by Django 4.2.7 on 2023-11-09 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReceitaApp', '0003_alter_receita_grau_de_dificuldade'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='imagem',
            field=models.ImageField(null=True, upload_to='imagens/'),
        ),
    ]
