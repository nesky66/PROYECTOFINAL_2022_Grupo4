# Generated by Django 4.0.6 on 2022-08-25 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_alter_categoria_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='post/'),
        ),
    ]
