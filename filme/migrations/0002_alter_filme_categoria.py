# Generated by Django 4.1.1 on 2022-09-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='categoria',
            field=models.CharField(choices=[('ACAO', 'Ação'), ('AVENTURA', 'Aventura'), ('ANIME', 'Animes'), ('OUTROS', 'Outros')], max_length=15),
        ),
    ]