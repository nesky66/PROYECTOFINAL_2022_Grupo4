# Generated by Django 4.0.6 on 2022-08-06 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_post_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='Imagen'),
        ),
    ]