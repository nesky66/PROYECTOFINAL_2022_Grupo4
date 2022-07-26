# Generated by Django 4.0.6 on 2022-08-08 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_alter_categoria_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='post',
            name='fecha_creation',
        ),
        migrations.RemoveField(
            model_name='post',
            name='fecha_update',
        ),
        migrations.AddField(
            model_name='categoria',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='categoria',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.RemoveField(
            model_name='post',
            name='categoria_id',
        ),
        migrations.AddField(
            model_name='post',
            name='categoria_id',
            field=models.ManyToManyField(to='post.categoria'),
        ),
    ]
