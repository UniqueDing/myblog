# Generated by Django 3.0.3 on 2020-02-15 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_delete_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='label',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
