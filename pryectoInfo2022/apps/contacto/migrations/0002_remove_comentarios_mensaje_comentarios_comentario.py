# Generated by Django 4.0.6 on 2022-08-26 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarios',
            name='mensaje',
        ),
        migrations.AddField(
            model_name='comentarios',
            name='comentario',
            field=models.TextField(null=True),
        ),
    ]
