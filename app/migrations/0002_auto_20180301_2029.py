# Generated by Django 2.0.2 on 2018-03-01 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='article',
            name='label',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
