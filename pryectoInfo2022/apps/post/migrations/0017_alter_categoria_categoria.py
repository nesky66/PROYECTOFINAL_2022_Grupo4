# Generated by Django 4.0.6 on 2022-08-09 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_rename_categoria_id_post_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='categoria',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
